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
 
#  ZOpenCVImageView.py
 
# 2018/05/05 Updated

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno


from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from SOL4Py.opencv.ZOpenCVImageView       import *

class ZOpenCVScrolledImageView(QScrollArea):

  def __init__(self, parent, filename=None, flags=cv2.IMREAD_COLOR):
    super(ZOpenCVScrolledImageView, self).__init__(parent)
    self.image_view = ZOpenCVImageView(parent, filename, flags)
    self.image_view.load_opencv_image(filename, flags)
    
    self.setWidget(self.image_view)
    
  def load_opencv_image(self, filename, flags = cv2.IMREAD_COLOR):    
    image = self.image_view.load_opencv_image(filename, flags)
    if image.all() != None:
      self.image_view.resize_to_image()
  

  def set_opencv_image(self, cvimage):
    self.image_view.set_opencv_image(cvimage)
      
  def get_opencv_image(self):
    return self.image_view.get_opencv_image()
    
  def get_qpixmap(self):
    return self.image_view.get_qpixmap()
    
  def get_image_view(self):
    return self.image_view
    
