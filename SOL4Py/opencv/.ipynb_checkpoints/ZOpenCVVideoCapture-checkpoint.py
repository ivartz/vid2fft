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
 
#  ZOpenCVVideoCapture.py
 
# 2018/05/05 Updated

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno

from SOL4Py.opencv.ZOpenCVImageConverter  import ZOpenCVImageConverter

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

class ZOpenCVVideoCapture:

  def __init__(self):
    self.target = 0
    self.video_capture   = cv2.VideoCapture()
    
  def open(self, target):
    self.target = target
    
    if isinstance(self.target, str):
      abspath = os.path.abspath(self.target)
      print("abspath:{}".format(abspath))
      if os.path.isfile(abspath):
        r = self.video_capture.open(abspath)
        if r == False:
          raise Error("Failed to open {}".format(abspath))
        else:
          print("Opened video_fille {}".format(abspath))
          return True
          
      else:
        raise FileNotFoundError(errno.ENOENT, 
              os.strerror(errno.ENOENT), abspath)
    elif isinstance(self.target, int):
      device_id = int(self.target)
     
      r = self.video_capture.open(device_id)
      if r == False:
        raise Error("Failed to open {}".format(device_id))
      else:
        print("Opened video_device {}".format(device_id))
        return True 
    else:
      return False
      
    
  def is_opened(self):
    return self.video_capture.isOpened()
    
  def close(self):
    self.video_capture.release()
    self.video_capture = None
    
  def set(self, prop_id, value):
    self.video_capture.set(prop_id, value)

  def get(self, prop_id):
    return self.video_capture.get(prop_id)
    
  def read(self):
    if self.is_opened():
      ret, frame = self.video_capture.read()
      if ret == True:
        return frame
      else:
        return None
        
    else:
      return None
  
  
  def close(self):
    if self.is_opened():
      self.video_capture.release()