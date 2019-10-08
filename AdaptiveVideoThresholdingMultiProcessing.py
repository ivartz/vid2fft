import sys
import os
import cv2
import traceback

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

from SOL4Py.ZApplication         import *
from SOL4Py.ZLabeledComboBox     import *
from SOL4Py.ZLabeledSlider       import *
from SOL4Py.ZApplicationView     import *
from SOL4Py.opencv.ZOpenCVImageView     import ZOpenCVImageView
from SOL4Py.opencv.ZOpenCVVideoCapture  import ZOpenCVVideoCapture
import multiprocessing as mp
import threading
from time import sleep, time

def cam_process(raw_video_queue, device=0):
  video_capture = ZOpenCVVideoCapture()
  video_capture.open(device)
  while True:
    if video_capture.is_opened():
        frame = video_capture.read()
        #raw_video_queue.put(frame)
        raw_video_queue.put_nowait(frame) # non-blocking


def start_cam_process(raw_video_queue, device=0):
  p = mp.Process(target=cam_process, args=(raw_video_queue, device))
  p.start()
  return p

def binarize_process(to_binarize_video_queue, \
                     binarize_video_settings_queue, \
                     binarized_video_queue):
  binarize_settings = None
  #binarize_settings = (11, 0, 0)
  while True:
    if (not binarize_video_settings_queue.empty()) and (binarize_settings == None):
      binarize_settings = binarize_video_settings_queue.get() # blocking
    elif (not binarize_video_settings_queue.empty()) and (binarize_settings != None):
      binarize_settings = binarize_video_settings_queue.get() # blocking
    if (not to_binarize_video_queue.empty()) and (binarize_settings != None):
      raw_frame = to_binarize_video_queue.get() # blocking
      
      if raw_frame.any() != None:
        gray_image = cv2.cvtColor(raw_frame, cv2.COLOR_RGB2GRAY)
        MAX_PIXEL_VALUE    = 255
        C                  = 9.0
        adaptive_method_id = binarize_settings[0]
        threshold_type_id  = binarize_settings[1]
        block_size         = binarize_settings[2]
        binarized_image    = cv2.adaptiveThreshold(gray_image, \
                                                   MAX_PIXEL_VALUE, \
                                                   adaptive_method_id, \
                                                   threshold_type_id, \
                                                   block_size, \
                                                   C);
        binarized_video_queue.put_nowait(binarized_image) # non-blocking

def start_binarize_process(to_binarize_video_queue, \
                           binarize_video_settings_queue, \
                           binarized_video_queue):
  p = mp.Process(target=binarize_process, \
                 args=(to_binarize_video_queue, \
                       binarize_video_settings_queue, \
                       binarized_video_queue))
  p.start()
  return p

class MainView(ZApplicationView):
  
  class BinarizedImageView(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)
  
  # Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    
    self.raw_video_queue = mp.Queue()
    self.to_binarize_video_queue = mp.Queue()
    self.binarized_video_queue = mp.Queue()
    
    # Binarize initial settings
    #self.block_size         = 11
    #self.adaptive_method_id = 0;
    #self.threshold_type_id  = 0;
    
    self.binarize_video_settings_queue = mp.Queue()
    #binarize_video_settings_queue.put_nowait((self.block_size, \
    #                                          self.adaptive_method_id, \
    #                                          self.threshold_type_id))
    
    self.time_snapshot_seconds = None # initialized to None . Used for rate limiting processing pipelines
    self.processing_rate_limit_hz = 20 # 30 Hz seems to be about the maximum if this camera
    
    self.raw_image_view  = ZOpenCVImageView(self)
    self.binarized_image_view = self.BinarizedImageView(self)

    self.add(self.raw_image_view)
    self.add(self.binarized_image_view)

    title = name
    self.setWindowTitle(title)
    
    self.show()
  
  def add_control_pane(self, fixed_width=220):
    # Control pane widget
    self.vpane = ZVerticalPane(self, fixed_width)
    
    #"""
    self.block_size         = 11
    self.adaptive_method_id = 0;
    self.threshold_type_id  = 0;
    #"""
    
    self.methods = {"ADAPTIVE_THRESH_MEAN_C": cv2.ADAPTIVE_THRESH_MEAN_C, 
                    "ADAPTIVE_THRESH_GAUSSIAN_C": cv2.ADAPTIVE_THRESH_GAUSSIAN_C}
    self.types   = {"THRESH_BINARY":  cv2.THRESH_BINARY  , 
                    "THRESH_BINARY_INV": cv2.THRESH_BINARY_INV }
    
    self.adaptive_method = ZLabeledComboBox(self.vpane, "AdaptiveMethod")
    self.adaptive_method.add_items(list(self.methods.keys() ))
    self.adaptive_method.add_activated_callback(self.adaptive_method_activated)
    
    self.threshold_type  = ZLabeledComboBox(self.vpane, "ThresholdType")
    self.threshold_type.add_items(list(self.types.keys()) )
    self.threshold_type.add_activated_callback(self.threshold_type_activated)
    
    self.labeled_slider = ZLabeledSlider(self.vpane, "BlockSize", take_odd =True,  
              minimum=3, maximum=43, value=self.block_size, fixed_width=200)
    self.labeled_slider.add_value_changed_callback(self.slider_value_changed)
    
    self.vpane.add(self.adaptive_method)
    self.vpane.add(self.threshold_type)    
    self.vpane.add(self.labeled_slider)

    self.set_right_dock(self.vpane)

  def slider_value_changed(self, value):
    self.block_size = int(value)
    if self.block_size % 2 == 0:
      # Block size should be odd.
      self.block_size = int((self.block_size * 2)/2 + 1)
    #print("slider_value_changed:{}".format(block_size))
    
    #self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
    
    settings = (self.adaptive_method_id, self.threshold_type_id, self.block_size)
    self.binarize_video_settings_queue.put_nowait(settings)
    
  def adaptive_method_activated(self, text):
    #print("adaptive_method_activated:{}".format(text))
    self.adaptive_method_id = self.methods[text]
    
    #self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
    
    settings = (self.adaptive_method_id, self.threshold_type_id, self.block_size)
    self.binarize_video_settings_queue.put_nowait(settings)
     
  def threshold_type_activated(self, text):
    #print("threshold_type_activated:{}".format(text))
    self.threshold_type_id = self.types[text]
    
    #self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
    
    settings = (self.adaptive_method_id, self.threshold_type_id, self.block_size)
    self.binarize_video_settings_queue.put_nowait(settings)
    
  # Read a frame from a video buffer of the video capture, and set it the image view to draw it on the imag view     
  def render(self):
    
    return_true = False
    #return_true = True
    #"""
    if not self.raw_video_queue.empty():
      raw_frame = self.raw_video_queue.get_nowait()
      
      if raw_frame.any() != None:
        self.raw_image_view.set_opencv_image(raw_frame)
        self.raw_image_view.update()
        
        # Send frame to processing queue
        # rate limited
        current_time_seconds = time()
        
        if self.time_snapshot_seconds == None:
          self.time_snapshot_seconds = current_time_seconds
        
        if current_time_seconds > self.time_snapshot_seconds: # Avoid dividing by zero
        
          #print(1/(current_time_seconds-self.time_snapshot_seconds))
          
          if ((1/(current_time_seconds-self.time_snapshot_seconds)) <= self.processing_rate_limit_hz): # Rate limit
          
            #print("Sending raw frame for further processing!")
            
            self.to_binarize_video_queue.put_nowait(raw_frame)
            
            self.time_snapshot_seconds = current_time_seconds
          
        
        return_true = True
      
    if not self.binarized_video_queue.empty():
      binarized_frame = self.binarized_video_queue.get_nowait()
      
      if binarized_frame.any() != None:
        self.binarized_image_view.set_opencv_image(binarized_frame)
        self.binarized_image_view.update()
        
        return_true = True
    #"""
    if return_true:
      return True
    else:
      return False
  
  def file_quit(self):
    self.terminated = True
    
  def closeEvent(self, ce):
    self.terminated = True

####
if main(__name__):
  #if __name__ == '__main__':
  try:
    name   = os.path.basename(sys.argv[0])
    applet = ZApplication(sys.argv)
        
    mainv  = MainView(name, 40, 40, 640, 480)

    mainv.show()
    
    cam_process = \
    start_cam_process(mainv.raw_video_queue, \
                      device=0)
    
    binarize_process = \
    start_binarize_process(mainv.to_binarize_video_queue, \
                           mainv.binarize_video_settings_queue, \
                           mainv.binarized_video_queue)
    
    applet.run(mainv)
    
    cam_process.terminate()
    binarize_process.terminate()
    
  except:
    traceback.print_exc()