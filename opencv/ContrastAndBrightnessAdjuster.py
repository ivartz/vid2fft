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
 
#  ContrastAndBrightnessAdjuster.py

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

  class ConvertedImageView(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)
      
    def load(self, filename):
      self.load_opencv_image(filename)
       
    def convert(self, alpha, beta):
      source_image = self.get_opencv_image()
      result = source_image.copy()
      cv2.convertScaleAbs(source_image, result, alpha, beta)
      self.set_opencv_image(result)
   
      self.update()
      
  #--------------------------------------------
  


  # MainView Constructor
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)

    filename = "../images/Cloud.png"
        
    # 1 Create first imageview.
    self.source_image_view = self.SourceImageView(self) 

    # 2 Create second imageview.
    self.converted_image_view = self.ConvertedImageView(self) 
  
    # 3 Load the file
    self.load_file(filename)
    
    # 4 Add two image views to a main_layout of this main view.
    self.add(self.source_image_view)
    self.add(self.converted_image_view)
    
    self.show()
  

  def add_control_pane(self, fixed_width=200):
    # Control pane widget
    self.vpane = ZVerticalPane(self, fixed_width)
     
    self.contrast   =  1
    self.brightness = 11
    
    self.contrast_slider = ZLabeledSlider(self.vpane, "Color", take_odd =False,  
              minimum=1, maximum=3, value=self.contrast)    
    self.contrast_slider.add_value_changed_callback(self.slider1_value_changed)
    self.vpane.add(self.contrast_slider)

    self.brightness_slider = ZLabeledSlider(self.vpane, "Contrast", take_odd =False,  
              minimum=0, maximum=100, value=self.brightness)    
    self.brightness_slider.add_value_changed_callback(self.slider2_value_changed)
    self.vpane.add(self.brightness_slider)
    

    self.set_right_dock(self.vpane)

  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_file(filename)
      
  def load_file(self, filename):
    self.source_image_view.load  (filename)
    self.converted_image_view.load(filename)
    
    # Apply convert method to the converted image view.
    self.converted_image_view.convert(self.contrast, self.brightness)
    
    self.set_filenamed_title(filename)
 
  
  def slider1_value_changed(self, value):
    self.contrast = int(value)
    self.converted_image_view.convert(int(self.contrast), int(self.brightness))

  def slider2_value_changed(self, value):
    self.brightness = int(value)
    self.converted_image_view.convert(int(self.contrast), int(self.brightness))
     
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

