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
 
#  ZLabeledSpinBox.py

# encoding:utf-8

import sys
import os
import traceback

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
 

#Horizontallabeled spinbox

class ZLabeledDoubleSpinBox(QWidget):
  # Constructor:
  # Creates a  spinbox with a label 
  
  def __init__(self, parent, label = "LabeledSpinBox", 
                     minimum=0, 
                     maximum=20, 
                     value=10, 
                     step =1,
                     fixed_width = 180):
    QWidget.__init__(self, parent)
    self.minimum  = minimum
    self.maximum  = maximum

    # Create a hbox to contain a spinbox and value-label.
    self.hlayout =  QHBoxLayout()

    # Create a label and spinbox.
    self.label  = QLabel(self)
    self.label.setText(label)
    self.spinbox = QDoubleSpinBox(self) 
    self.spinbox.setSingleStep(step)
    self.spinbox.setRange(self.minimum, self.maximum)
    self.spinbox.setValue(value)
    
    self.hlayout.addWidget(self.label)
    self.hlayout.addStretch()
    self.hlayout.addWidget(self.spinbox)
    self.setLayout(self.hlayout)


  def add_value_changed_callback(self, callback):
    self.spinbox.valueChanged(callback)


  def get_spinbox(self):
    return self.spinbox


  def get_value(self):
    return self.spinbox.value()

  def set_value(self):
    return self.spinbox.setValue()


  def set_range(self, min, max):  
    self.spinbox.setRange(min, max)


  def set_label(self, value):
    self.label.setText(str(value))
        


