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
from time import sleep

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

class MainView(ZApplicationView):
  
  class BinarizedImageView(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)
      
    def load_source_image(self, source_image):
      image =  cv2.GaussianBlur(source_image, (3,3), 0, 0, borderType = cv2.BORDER_DEFAULT );
      #image =  cv2.GaussianBlur(source_image, (3,3), 0, 0)

      self.gray_image = cv2.cvtColor(source_image, cv2.COLOR_RGB2GRAY)
             
    def binarize(self, adaptive_method_id, threshold_type_id, block_size):
      MAX_PIXEL_VALUE = 255
      C               = 9.0
    
      binarized_image = cv2.adaptiveThreshold(self.gray_image,  MAX_PIXEL_VALUE, 
          adaptive_method_id, threshold_type_id, block_size,  C);
          
      #return binarized_image
      self.set_opencv_image(binarized_image)
      self.update()
  
  # Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    
    self.raw_video_queue = mp.Queue()
    
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
    
    self.block_size         = 11
    self.adaptive_method_id = 0;
    self.threshold_type_id  = 0;

    
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
    self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
    
  def adaptive_method_activated(self, text):
    #print("adaptive_method_activated:{}".format(text))
    self.adaptive_method_id = self.methods[text]
    
    self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
     
  def threshold_type_activated(self, text):
    #print("threshold_type_activated:{}".format(text))
    self.threshold_type_id = self.types[text]
    self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
    
  # Read a frame from a video buffer of the video capture, and set it the image view to draw it on the imag view     
  def render(self):
    
    #return_true = False
    
    if not self.raw_video_queue.empty():
      raw_frame = self.raw_video_queue.get_nowait()
      
      if raw_frame.any() != None:
        self.raw_image_view.set_opencv_image(raw_frame)
        self.raw_image_view.update()
        
        
        self.binarized_image_view.load_source_image(raw_frame)
        self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
        
        
        return True
      
    """
      
    if not self.binarized_video_queue.empty():
      binarized_frame = self.binarized_video_queue.get_notwait()
      if binarized_frame.any() != None:
        self.binarized_image_view.set_opencv_image(binarized_frame)
        self.binarized_image_view.update()
        return_true = True
    
    if return_true:
      return True
    else:
      return False
    """
    return False
    
  """
  def load_file(self, filename):
    self.image_view_3.load(filename)
    self.set_filenamed_title(filename)
 """
  
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
    
    p = start_cam_process(mainv.raw_video_queue, device=0)
    
    applet.run(mainv)
    
    p.terminate()
    
  except:
    traceback.print_exc()