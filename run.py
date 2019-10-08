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
#from SOL4Py.opencv.ZOpenCVVideoCapture  import ZOpenCVVideoCapture
from multiprocessing import Queue
#import threading
from time import time
import numpy as np

from process import cam_process, \
                    start_cam_process, \
                    dft_process, \
                    start_dft_process

class MainView(ZApplicationView):
  # Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height, layout=Z.Grid)
    
    self.raw_video_queue = Queue()
    self.to_dft_video_queue = Queue()
    self.dft_settings_queue = Queue()
    
    self.dft_settings_queue.put_nowait([30]) # temporary
    
    self.dft_magnitude_unfiltered_video_queue = Queue()
    self.dft_magnitude_filtered_video_queue = Queue()
    self.filtered_video_queue = Queue()
    
    self.time_snapshot_seconds = None # initialized to None . Used for rate limiting processing pipelines
    self.processing_rate_limit_hz = 5
    
    self.raw_image_view  = ZOpenCVImageView(self)
    self.dft_magnitude_unfiltered_image_view  = ZOpenCVImageView(self)
    self.dft_magnitude_filtered_image_view  = ZOpenCVImageView(self)
    self.filtered_image_view  = ZOpenCVImageView(self)
    
    #self.grid = ZGridLayouter(self)
    
    self.main_layouter.add(self.raw_image_view, 0, 0)
    self.main_layouter.add(self.dft_magnitude_unfiltered_image_view, 0, 1)
    self.main_layouter.add(self.dft_magnitude_filtered_image_view, 1, 1)
    self.main_layouter.add(self.filtered_image_view, 1, 0)

    title = name
    self.setWindowTitle(title)
    
    self.show()
  #"""
  def add_control_pane(self, fixed_width=220):
    # Control pane widget
    self.vpane = ZVerticalPane(self, fixed_width)
    
    self.filter_width_div_two         = 30
    #self.adaptive_method_id = 0;
    #self.threshold_type_id  = 0;
    """
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
    """
    self.labeled_slider = ZLabeledSlider(self.vpane, "Filter width // 2 ", take_odd = True,  
              minimum=0, maximum=480//2, value=self.filter_width_div_two, fixed_width=200)
    self.labeled_slider.add_value_changed_callback(self.slider_value_changed)
    
    #self.vpane.add(self.adaptive_method)
    #self.vpane.add(self.threshold_type)    
    self.vpane.add(self.labeled_slider)

    #self.set_right_dock(self.vpane)
    #self.grid = ZGridLayouter(self)
    
    self.main_layouter.add(self.vpane, 1, 2)

  def slider_value_changed(self, value):
    self.block_size = int(value)
    #if self.block_size % 2 == 0:
    #  # Block size should be odd.
    #  self.block_size = int((self.block_size * 2)/2 + 1)
    #print("slider_value_changed:{}".format(block_size))
    
    #self.binarized_image_view.binarize(self.adaptive_method_id, self.threshold_type_id, self.block_size)
    """
    # Send frame to processing queue rate limited
    current_time_seconds = time()
    
    if self.time_snapshot_seconds == None:
      self.time_snapshot_seconds = current_time_seconds
    
    if ((1/(current_time_seconds-self.time_snapshot_seconds)) <= self.processing_rate_limit_hz): # Rate limit
        """
        
    settings = [self.block_size]
    
    self.dft_settings_queue.put_nowait(settings)
  #"""
  """
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
  """
  # Read a frame from a video buffer of the video capture, and set it the image view to draw it on the imag view     
  def render(self):
    
    return_true = False

    if not self.raw_video_queue.empty():
      raw_frame = self.raw_video_queue.get_nowait()
      
      if raw_frame.any() != None:
        self.raw_image_view.set_opencv_image(raw_frame)
        self.raw_image_view.update()
        
        # Send frame to processing queue rate limited
        current_time_seconds = time()
        
        if self.time_snapshot_seconds == None:
          self.time_snapshot_seconds = current_time_seconds
        
        if current_time_seconds > self.time_snapshot_seconds: # Avoid dividing by zero
        
          #print(1/(current_time_seconds-self.time_snapshot_seconds))
          
          if ((1/(current_time_seconds-self.time_snapshot_seconds)) <= self.processing_rate_limit_hz): # Rate limit
          
            #print("Sending raw frame for further processing!")
            
            self.to_dft_video_queue.put_nowait(raw_frame)
            
            self.time_snapshot_seconds = current_time_seconds
        
        return_true = True
      
    if not self.dft_magnitude_unfiltered_video_queue.empty():
      dft_magnitude_unfiltered_frame = \
      self.dft_magnitude_unfiltered_video_queue.get_nowait()
      
      if dft_magnitude_unfiltered_frame.any() != None:
        self.dft_magnitude_unfiltered_image_view.set_opencv_image(np.uint8(dft_magnitude_unfiltered_frame))
        self.dft_magnitude_unfiltered_image_view.update()
        
        return_true = True
    
    if not self.dft_magnitude_filtered_video_queue.empty():
      dft_magnitude_filtered_frame = \
      self.dft_magnitude_filtered_video_queue.get_nowait()
      
      if dft_magnitude_filtered_frame.any() != None:
        self.dft_magnitude_filtered_image_view.set_opencv_image(np.uint8(dft_magnitude_filtered_frame))
        self.dft_magnitude_filtered_image_view.update()
        
        return_true = True

    if not self.filtered_video_queue.empty():
      filtered_video_frame = \
      self.filtered_video_queue.get_nowait()
      
      if filtered_video_frame.any() != None:
        self.filtered_image_view.set_opencv_image(np.uint8(filtered_video_frame))
        self.filtered_image_view.update()
        
        return_true = True    
    
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
        
    mainv  = MainView(name, 40, 40, 2*640, 2*480)
    
    cam_process = \
    start_cam_process(mainv.raw_video_queue, \
                      device=0)
    
    dft_process = \
    start_dft_process(mainv.to_dft_video_queue, \
                      mainv.dft_settings_queue, \
                      mainv.dft_magnitude_unfiltered_video_queue, \
                      mainv.dft_magnitude_filtered_video_queue, \
                      mainv.filtered_video_queue)
    
    mainv.show()
    
    applet.run(mainv)
    
    cam_process.terminate()
    dft_process.terminate()
    
  except:
    traceback.print_exc()