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
 
#  ZVerticalPane.py

# encoding: utf-8

import sys
import os
import traceback

from PyQt5 import QtCore, QtWidgets, QtGui

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
 
    
class ZVerticalPane(QWidget):

  def __init__(self, parent, fixed_width, alignment=Qt.AlignTop):
    super(ZVerticalPane, self).__init__(parent)
    self.layout = QVBoxLayout(self)
    self.layout.setAlignment(alignment)

    self.set_fixed_width(fixed_width)
     
  def add(self, widget, x=0, y=0):
    #print("ZVerticalLayouter {},{}".format(x, y))
    self.layout.addWidget(widget)

  def get_layout(self):
    return self.layout
 
  def set_fixed_width(self, fixed_width):
    if fixed_width > 0:
      self.setMinimumWidth(fixed_width)
      self.setMaximumWidth(fixed_width)
    
