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
 
#  ZOpenCVCroppedImageReader.py


# encoding: utf-8

import sys
import os
import traceback

# We use OpenCV-4.0.X library

import cv2
from SOL4Py.opencv.ZOpenCVImageReader       import *

class ZOpenCVCroppedImageReader(ZOpenCVImageReader):

  def __init__(self, to_rgb = True):
    super(ZOpenCVCroppedImageReader, self).__init__(to_rgb)


  def crop_max_square_region(self, image, scale=None):
    h, w = image.shape[:2]
    print ("w:" + str(w) + " h:" + str(h))
    
    # Get a size of a maximum square region of the image 
    if w > h:
      s = h
    else:
      s = w
    y = int( (h - s)/2 )
    x = int( (w - s)/2 )

    cropped = image[y:y+s, x:x+s]

    if scale != None:
       cropped  = cv2.resize(cropped, dsize=scale)

    return cropped


