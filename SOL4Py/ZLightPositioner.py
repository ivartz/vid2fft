#/******************************************************************************
# 
#  Copyright (c) 2019 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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
 
#  ZLightPositioner.py

# encoding:utf-8

import sys
import os
import traceback

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

from SOL4Py.ZPositioner import * 

class ZLightPositioner(ZPositioner):
  
  def __init__(self, parent, title = "LightPositioner", value_labels = ["X", "Y", "Z"],
                     minimax=[0, 255],
                     values=[0, 128, 128], 
                     fixed_width = 260):
                     
    ZPositioner.__init__(self, parent, title, value_labels,
                     minimax, 
                     values, 
                     fixed_width)


  def set_light_position(self, x, y, z):
    self.set_values([x, y, z])
    self.update()
    


