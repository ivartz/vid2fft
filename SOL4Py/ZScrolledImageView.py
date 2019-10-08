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
#  ZScrolledImageView.py

# encodig: utf-8

import sys
import os
import traceback

from SOL4Py.ZImageView import *
from PyQt5.QtWidgets   import *
from PyQt5.QtGui       import *
from PyQt5.QtCore      import *
from SOL4Py.ZImageView import *

#---------------------------------------------------------------------

class ZScrolledImageView(QScrollArea):

  def __init__(self, parent, x, y, width, height, keepAspectRatio=True):
    super(ZScrolledImageView, self).__init__(parent)
    self.image_view = ZImageView(parent, x, y, width, height, keepAspectRatio)
    self.setWidget(self.image_view)
    
  def load_image(self, filename):
    self.image_view.load_image(filename) # 

  def set_plotted_figure(self):
    filename = "temp.png"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, filename)
    plt.savefig(fullpath)
    plt.close()
    sef.image_view.load_image(fullpath)
    os.remove(fullpath)
    

  def get_image_view(self):
    return self.image_view

  def get_image(self, width, height):
    return self.image_view.get_image(width, height)
    
  def rescale(self, percentage):
    self.image_view.rescale(percentage)
    
  def file_save(self, filename):
    self.image_view.file_save(filename)

  def set_image(self, ndarray):
    self.image_view.set_image(ndarray)
        
  