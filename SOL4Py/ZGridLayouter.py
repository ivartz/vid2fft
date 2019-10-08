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

# 2018/05/05 Updated add method.

#  ZGridLayouter.py

# encoding: utf-8

import sys
import os
import traceback

from PyQt5 import QtCore, QtWidgets, QtGui

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
 
# Grid layouter which can be used as a central widget of QMainWindow. 

class ZGridLayouter(QWidget):
  def __init__(self, parent):
    super(ZGridLayouter, self).__init__(parent)
    print("ZGridLayout")
    self.layout = QGridLayout(self)
    self.setLayout(self.layout)
    
    # The parent should be an instance of QMainWindow. 
    parent.setCentralWidget(self)
    self.show()
    
    
  def add_widget(self, widget, x, y):
    print("ZGridLayout {}, {}".format(x, y))
    self.layout.addWidget(widget, x, y)
    
  # 
  def add(self, widget, x, y, spanx=1, spany=1):
    #print("ZGridLayout {}, {}".format(x, y))
    self.layout.addWidget(widget, x, y, spanx, spany)

  def get_layout(self):
    return self.layout
   
  def get_widget(self):
    return self

