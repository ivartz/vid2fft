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
 
#  ZOpenCVImageReader.py


# encoding: utf-8

import sys
import os
import traceback

# We use OpenCV-4.0.X library

import cv2

class ZOpenCVImageReader:

  def __init__(self, to_rgb = True):
    # Flag to convert bgr to rgb.
    self.bgr_to_rgb = to_rgb
    
  def read(self, filename="", flag=cv2.IMREAD_COLOR):
    abspath = os.path.abspath(filename)
    print("abspath:{}".format(abspath))
   
    if not os.path.isfile(abspath):
      raise FileNotFoundError(errno.ENOENT, 
              os.strerror(errno.ENOENT), abspath)

    image = cv2.imread(abspath, flag)
    if self.bgr_to_rgb == True:
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

