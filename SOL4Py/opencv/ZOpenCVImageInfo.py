#/******************************************************************************
# 
#  Copyright (c) 2019 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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
 
#  ZOpenCVImageInfo.py

# encodig: utf-8

import numpy as np
import cv2

from SOL4Py.opengl.ZOpenGLImageInfo import *


class ZOpenCVImageInfo:
  
  def __init__(self):
    pass
    
  # Returns ZOpenGLImageInfo from the cv2.Mat image.
  def getImageInfo(self, image, flip = False, convert_to_rgb=False):
  
    bgr = image;
 
    if len(image.shape) == 3:
      height, width, channels = image.shape[:3]
    else:
      height, width = image.shape[:2]
      channels = 1
 
    if channels == 1:
      # if image is grayscale, we convert  to bgra 
      bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR);

    #dtype     = image.dtype.bytes
    if flip == True:
      bgr = cv2.flip(bgr, 0)

    if convert_to_rgb == True:
      rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    else:
      rgb = bgr

    imageInfo = ZOpenGLImageInfo()
 
    imageInfo.depth    = channels * 8; #dtype ; 
    imageInfo.channels = channels;
    imageInfo.width    = width;
    imageInfo.height   = height;
    imageInfo.format   = GL_RGB
     
    imageInfo.imageSize = rgb.nbytes  # width * height * 4; #sizeof(uint32); //Image byte size
    imageInfo.imageData = rgb;

    return imageInfo
    
