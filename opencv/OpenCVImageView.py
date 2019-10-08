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
 
#  OpenCVImageView.py
 
# 2018/05/01

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *

sys.path.append('../')

from SOL4Py.opencv.ZOpenCVImageView           import ZOpenCVImageView

#---------------------------------------------------------------------
# Unit test
#
if __name__ == '__main__':
  try:
    applet = QApplication(sys.argv)
    image_view = ZOpenCVImageView(parent=None)
  
    image_view.load_opencv_image("../images/flower.png", cv2.IMREAD_GRAYSCALE)
    image_view.setGeometry(40, 40, 400, 300)
    image_view.show()
  
    applet.exec_()
  
  except:
    traceback.print_exc()
