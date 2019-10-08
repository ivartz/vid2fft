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
 
#  GridLayoutOpenCVImageView.py
 
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

from SOL4Py.ZImageView           import ZImageView
from SOL4Py.opencv.ZOpenCVImageView     import ZOpenCVImageView

#---------------------------------------------------------------------
#
if __name__ == '__main__':
  applet  = QApplication(sys.argv)
  appview = QWidget()
  appview.setWindowTitle(sys.argv[0])
  grid    = QGridLayout(appview)
  image_views = [None, None, None, None, None, None]
  filenames   = ["../images/flower.png", "../images/flower1.jpg", 
                 "../images/flower2.jpg", "../images/flower3.jpg",
                 "../images/flower7.jpg"]

  for i in range(len(filenames)):  
    image_views[i] = ZOpenCVImageView(appview) #, 0, 0, 400, 300)
    image_views[i].load_opencv_image(filenames[i], i % 3)
    y = int(i % 3)
    x = int(i / 3)
    
    grid.addWidget(image_views[i], x, y)
  
  appview.setGeometry(40, 40, 800, 400)
  appview.show()
  
  applet.exec_()

