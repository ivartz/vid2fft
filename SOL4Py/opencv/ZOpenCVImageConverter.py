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
 
#  ZOpenCVImageConverter.py

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno

class ZOpenCVImageConverter:

  def __init__(self):
    pass
    
  # Convert bgr image read by cv2.imread to rgb image to paint it in 
  # PyQt5 world.
  def convert_to_rgb(self, image):
    # For simplicity, in case of gray scale, we convert it to RGB
    # This is the case of gray scale
    if len(image.shape) == 2:
      rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
      return rgb
      
    # If lenght of image.shape is 3.
    if len(image.shape) == 3:
      height, width, channels = image.shape
      rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      return rgb

