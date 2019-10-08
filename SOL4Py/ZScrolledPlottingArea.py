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
# 2018/08/30 Added gcf parameter to Constructor:
#  def __init__(self, parent, width, height, gcf=False):

# encodig: utf-8

import sys
import os
import traceback

import cv2
import errno


from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from SOL4Py.ZPlottingArea  import *


class ZScrolledPlottingArea(QScrollArea):
  # 2018/08/30 Added gcf parameter
  def __init__(self, parent, width, height, figure=None):
    super(ZScrolledPlottingArea, self).__init__(parent)
 
    self.plotting_area = ZPlottingArea(self, width, height, figure)
    self.setWidget(self.plotting_area)
    
  def add(self, index):
    return self.plotting_area.add(index)
    
  def get_plotting_area(self):
    return self.plotting_ara
    
  def get_figure(self):
    return self.plotting_area.get_figure()
    
  def set_figure(self, figure):
    self.setWidget(None)
    self.plotting_area.deleteLater()
    self.update()
    size = self.plotting_area.size()
    
    self.plotting_area =  ZPlottingArea(self, size.width(), size.height(), figure)
    self.setWidget(self.plotting_area)
    
    
  def clear(self):
    self.plotting_area.clear()
    self.update()

  def subplot(self, x, y, i):
    self.plotting_area.subplot(x, y, i)
    
