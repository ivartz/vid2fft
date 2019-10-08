#/******************************************************************************
# 
#  Copyright (c) 2018 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/

#  SimpleBlobDetector.py

# encodig: utf-8

import sys
import os
import cv2
import traceback


from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

# 
sys.path.append('../')

from SOL4Py.ZApplicationView import *

from SOL4Py.ZLabeledComboBox import ZLabeledComboBox
from SOL4Py.ZLabeledSlider   import ZLabeledSlider
from SOL4Py.opencv.ZOpenCVImageView import ZOpenCVImageView  
from SOL4Py.ZVerticalPane    import ZVerticalPane

 
class MainView(ZApplicationView):
  # Inner classes
  #--------------------------------------------
  class SourceImageView(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)

    def load(self, filename):
      self.load_opencv_image(filename)
      self.update()

  class DetectedImageView(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)
      
    def load(self, filename):
      source_image = self.load_opencv_image(filename)
      self.gray_image = cv2.cvtColor(source_image, cv2.COLOR_RGB2GRAY)
             
    def detect(self, minDist, minArea, maxArea):
      source_image = self.get_opencv_image()
      
      params = cv2.SimpleBlobDetector_Params()
      
      params.thresholdStep = 10.0
      params.minThreshold = 50.0
      params.maxThreshold = 220.0
 
      params.filterByArea = True
      params.minArea = minArea
      params.maxArea = maxArea

      params.filterByColor = True
      params.blobColor     = 0

      params.filterByCircularity = True
      params.minCircularity = 0.5

      params.filterByConvexity = True
      params.minConvexity = 0.8
 
      params.filterByInertia = True
      params.minInertiaRatio = 0.1
 
      params.minRepeatability = 2
      params.minDistBetweenBlobs= 5.0
      params.minDistBetweenBlobs= float(minDist)

      detector = cv2.SimpleBlobDetector_create(params)
      keypoints = detector.detect(self.gray_image);
        
      out_image = cv2.drawKeypoints(source_image, keypoints, 
              None, (0, 0, 255), 
              cv2.DrawMatchesFlags_DRAW_RICH_KEYPOINTS )

      self.set_opencv_image(out_image)
      self.update()
      
  #--------------------------------------------
  


  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)

    filename = "../images/cat.jpg"
    
    # 1 Create first imageview.
    self.source_image_view = self.SourceImageView(self) 

    # 2 Create second imageview.
    self.detectd_image_view = self.DetectedImageView(self) 
  
    # 3 Load the file
    self.load_file(filename)
      
    # 4 Add two image views to a main_layout of this main view.
    self.add(self.source_image_view)
    self.add(self.detectd_image_view)

    self.show()
  

  def add_control_pane(self, fixed_width=220):
    # Control pane widget

    self.vpane = ZVerticalPane(self, fixed_width)
    
    self.minDist  = 9;
    self.minArea  = 15;
    self.maxArea  = 131
        
    self.minDistance_slider = ZLabeledSlider(self.vpane, "MinDistanceBetweenBlob", take_odd =False,  
              minimum=5, maximum=100, value=self.minDist, fixed_width=200)
    self.minDistance_slider.add_value_changed_callback(self.minDistance_value_changed)


    self.minArea_slider = ZLabeledSlider(self.vpane, "MinArea", take_odd =False,  
              minimum=1, maximum=100, value=self.minArea, fixed_width=200)
    self.minArea_slider.add_value_changed_callback(self.minArea_value_changed)
    
    self.maxArea_slider = ZLabeledSlider(self.vpane, "MaxArea", take_odd =False,  
              minimum=100, maximum=200, value=self.maxArea, fixed_width=200)
    self.maxArea_slider.add_value_changed_callback(self.maxArea_value_changed)
    
    self.vpane.add(self.minDistance_slider)
    self.vpane.add(self.minArea_slider)
    self.vpane.add(self.maxArea_slider)
    
    self.set_right_dock(self.vpane)

  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_file(filename)
      
  def load_file(self, filename):
    self.source_image_view.load(filename)
    self.detectd_image_view.load(filename)
    
    self.detectd_image_view.detect(self.minDist, self.minArea, self.maxArea)

    self.set_filenamed_title(filename)
      
  
  def minDistance_value_changed(self, value):
    self.minDist= int(value)
    self.detectd_image_view.detect(self.minDist, self.minArea, self.maxArea)
     
  def minArea_value_changed(self, value):
    self.minArea = int(value)
    self.detectd_image_view.detect(self.minDist, self.minArea, self.maxArea)

  def maxArea_value_changed(self, value):
    self.maxArea = int(value)
    self.detectd_image_view.detect(self.minDist, self.minArea, self.maxArea)


     
#*************************************************
#    
if main(__name__):
  try:
    app_name  = os.path.basename(sys.argv[0])
    applet    = QApplication(sys.argv)
  
    main_view = MainView(app_name, 40, 40, 900, 380)
    main_view.show ()

    applet.exec_()

  except:
     traceback.print_exc()
     pass

