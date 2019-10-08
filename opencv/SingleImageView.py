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

#  SingleImageView.py

# encodig: utf-8

import sys
import os
import traceback

#from PyQt5.QtCore    import *
#from PyQt5.QtWidgets import *
#from PyQt5.QtGui     import *

sys.path.append('../')

from SOL4Py.ZLabeledComboBox     import *
from SOL4Py.ZLabeledSlider       import *
from SOL4Py.ZApplicationView     import *
from SOL4Py.opencv.ZOpenCVImageView     import ZOpenCVImageView
 
class MainView(ZApplicationView):

  def __init__(self, title, x, y, width, height):
    super(MainView, self).__init__(title, x, y, width, height)
       
    filename = "../images/flower.png"
    
    # 1 Create an imageview in the main_widget 
    self.image_view = ZOpenCVImageView(self)
    
    # 2 Load opencv image into the imageview.
    self.image_view.load_opencv_image(filename)

    # 3 Add the imageview to the main_layout
    self.add(self.image_view)

    self.set_filenamed_title(filename)
    
    self.show()
       
  # Default file_open method to read an image file by using ZOpenCVImageReader
  # and set the image read to the first area of ZDrawingArea.
  def file_open(self):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getOpenFileName(self,"FileOpenDialog", "",
                     "All Files (*);;Image Files (*.png;*jpg;*.jpeg)", options=options)
    if filename:
      self.image_view.load_opencv_image(filename)
      self.set_filenamed_title(filename)
      
####
if main(__name__):
  try:
    name   = os.path.basename(sys.argv[0])
    applet = QApplication(sys.argv)
        
    mainv  = MainView(name, 40, 40, 640,480)
    mainv.show ()

    applet.exec_()

  except:
    traceback.print_exc()

