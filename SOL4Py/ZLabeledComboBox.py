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
 
#  ZLabeledComboBox.py

# encoding: utf-8

import sys
import os
import traceback

from PyQt5 import QtCore, QtWidgets, QtGui

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
 

class ZLabeledComboBox(QWidget):
  def __init__(self, parent, label, orientation=Qt.Vertical, alignment=Qt.AlignLeft, adjust_policy=True):
    #super(ZLabeledComboBox, self).__init__(parent)
    QWidget.__init__(self, parent)

    self.combobox = QComboBox(self)
    
    # 2018/05/01
    if adjust_policy == True:
      self.set_size_adjust_policy()
    
    self.label = QLabel(self)
    self.label.setText(label)
    
    if orientation == Qt.Vertical:
      self.layout = QVBoxLayout()
    if orientation == Qt.Horizontal:
      self.layout = QHBoxLayout()
      
    self.layout.addWidget(self.label)
    self.layout.addWidget(self.combobox)
    self.layout.setAlignment(alignment)
    
    self.setLayout(self.layout)

  def add(self, widget):
    self.layout.addWidget(widget)
    
  def get_combobox(self):
    return self.combobox

  def add_items(self, items):
    # 2018/05/01 Modified.
    items = list(items)
    if items != None and isinstance(items, list):
      for i in range(len(items)):  
        self.combobox.addItem(str(items[i]))

  def add_item(self, item):
    if item != None and isinstance(item, str):
      self.combobox.addItem(str(item))
    
  def get_current_text(self):
    return self.combobox.currentText()

  def set_current_text(self, index):
    self.combobox.setCurrentIndex(int(index))

  def set_label(self, value):
    self.label.setText(str(value))

  
  # Register a combobox activated callback to the self.combobox.
  def add_activated_callback(self, callback):
    self.combobox.activated[str].connect(callback)
     
  # Sample comobobox activate callback. 
  def activated(self, text):
    print("activated:{}".format(text))
        
  def set_size_adjust_policy(self):
    self.combobox.setSizeAdjustPolicy(QComboBox.AdjustToContents)    
    
  def setFont(self, font):
    self.label.setFont(font)
    self.combobox.setFont(font)
    
