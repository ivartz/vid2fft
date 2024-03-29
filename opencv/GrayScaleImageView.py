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
 
#  GrayScaleImageView.py

# encodig: utf-8

import sys
import os
import traceback

sys.path.append('../')

from SOL4Py.ZApplicationView  import *
from SOL4Py.opencv.ZOpenCVImageView  import *
 
class MainView(ZApplicationView):
  
  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
      
    filename = "../images/flower.png"

    self.image_views = [None, None]

    self.flags = [cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE]

    for i in range(len(self.image_views)):
      self.image_views[i]  = ZOpenCVImageView(self)
      self.add(self.image_views[i])
    
    self.load_image(filename)
    
    self.show()
           
  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.load_image(filename)
  
  def load_image(self, filename): 
    for i in range(len(self.image_views)):
      self.image_views[i]. load_opencv_image(filename, self.flags[i])
    
    self.set_filenamed_title(filename)

####
if main(__name__):
  try:
    name  = os.path.basename(sys.argv[0])
    applet= QApplication(sys.argv)
    
    mainv = MainView(name, 40, 40, 800,360)
    mainv.show ()
    
    applet.exec_()

  except:
    traceback.print_exc()

