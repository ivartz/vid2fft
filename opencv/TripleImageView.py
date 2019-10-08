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
 
#  TripleImageView.py

# encodig: utf-8

import sys
import os
import cv2
import traceback

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.opencv.ZOpenCVImageView  import ZOpenCVImageView  
 

class MainView(ZApplicationView):

  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
    
    self.image_views = [None, None, None]
    
    filenames = ["../images/flower.png", 
                 "../images/flower5.jpg", 
                 "../images/flower7.jpg"]
    flags     = [cv2.IMREAD_COLOR, 
                 cv2.IMREAD_GRAYSCALE, 
                 cv2.IMREAD_UNCHANGED]

    # Get the main horizontal layout from the parent ZApplicationView.    

    # Create imageviews, load images from the filenames, and add those imageviews to the main layout.
    for i in range(len(self.image_views)) :
      self.image_views[i] = ZOpenCVImageView(self)
      self.image_views[i].load_opencv_image(filenames[i], flags[i] )
      self.add(self.image_views[i])

    self.show()
    
####
    
if main(__name__):
  try:
    name   = os.path.basename(sys.argv[0])
    applet = QApplication(sys.argv)
  
    main_view  = MainView(name, 40, 40, 900, 380)
    main_view.show ()

    applet.exec_()

  except:
    traceback.print_exc()

