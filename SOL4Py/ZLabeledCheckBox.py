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
 
#  ZLabeledCheckBox.py

# encoding:utf-8

import sys
import os
import traceback

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
 

#Horizontallabeled spinbox

class ZLabeledCheckBox(QWidget):
  # Constructor:
  # Creates a  spinbox with a label 
  
  def __init__(self, parent, label = "LabeledCheckBox", 
                     step =1,
                     fixed_width = 180):
    QWidget.__init__(self, parent)

    # Create a hbox to contain a spinbox and value-label.
    self.hlayout =  QHBoxLayout()

    # Create a label and spinbox.
    self.label  = QLabel(self)
    self.label.setText(label)
    self.checkbox = QCheckBox(self) 
    
    self.hlayout.addWidget(self.label)
    self.hlayout.addStretch()
    self.hlayout.addWidget(self.checkbox)
    self.setLayout(self.hlayout)


  def add_state_changed_callback(self, callback):
    self.checkbox.stateChanged(callback)


  def get_checkbox(self):
    return self.chekcbox


  def is_checked(self):
    return self.checkbox.isChecked()

  def set_state(self, st):
    self.checkbox.set_state(st)


  def set_label(self, value):
    self.label.setText(str(value))
        


