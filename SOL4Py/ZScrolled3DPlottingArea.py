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
 
#  ZScrolledPlottingArea.py
 
# 2018/05/05 Updated

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno


from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from SOL4Py.Z3DPlottingArea  import *


class ZScrolled3DPlottingArea(QScrollArea):

  def __init__(self, parent, width, height):
    super(ZScrolled3DPlottingArea, self).__init__(parent)
    self.plotting_area = Z3DPlottingArea(self, width, height)
    self.setWidget(self.plotting_area)
   
  def add(self, index):
    return self.plotting_area.add(index)
    
  def get_plotting_area(self):
    return self.plotting_ara
    
  def get_figure(self):
    return self.plotting_area.get_figure()
    
  def get_ax(self):
    return self.plotting_area.get_ax()
    
