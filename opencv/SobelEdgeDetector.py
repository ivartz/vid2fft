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

#  SobelEdgeDetector.py

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

    def detect(self, ksize):
      ksize = int(ksize)

      gradX = cv2.Sobel(self.gray_image, -1, 1, 0, ksize=ksize)
      gradY = cv2.Sobel(self.gray_image, -1, 0, 1, ksize=ksize)

      absGradX = cv2.convertScaleAbs(gradX)
      absGradY = cv2.convertScaleAbs(gradY)

      detected_image = cv2.addWeighted( absGradX, 0.5, absGradY, 0.5, 0)
      self.set_opencv_image(detected_image)
      self.update()
      
  #--------------------------------------------
  


  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)

    filename = "../images/ClassicCar.png"
    
    # 1 Create first imageview.
    self.source_image_view = self.SourceImageView(self) 

    # 2 Create second imageview.
    self.detected_image_view = self.DetectedImageView(self) 
  
    # 3 Load the file
    self.load_file(filename)
      
    # 4 Add two image views to a main_layout of this main view.
    self.add(self.source_image_view)
    self.add(self.detected_image_view)

    self.show()
  
  # Add control pane to MainView
  def add_control_pane(self, fixed_width=200):
    # Control pane widget
    self.ksize = 5
    self.vpane = ZVerticalPane(self, fixed_width)
    self.labeled_slider = ZLabeledSlider(self.vpane, "KernelSize", take_odd =True,  
              minimum=0, maximum=33, value=self.ksize)
    
    self.labeled_slider.add_value_changed_callback(self.slider_value_changed)
    self.vpane.add(self.labeled_slider)

    self.set_right_dock(self.vpane)

  # Show FileOpenDialog and select an image file.
  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_file(filename)
      
  def load_file(self, filename):
    self.source_image_view.load(filename)
    self.detected_image_view.load(filename)
    self.detected_image_view.detect(int(self.ksize))
    self.set_filenamed_title(filename)
      
  # Slider value changed callback.
  def slider_value_changed(self, value):
    self.ksize = int(value)
    if self.ksize % 2 == 0:
      self.ksize = (self.ksize * 2)/2 + 1
      # Kernel size should be odd.
    print("slider_value_changed:{}".format(self.ksize))
    self.detected_image_view.detect(int(int(self.ksize)))
     
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

