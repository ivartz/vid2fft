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
 
#  ZCSVTableView.py

# encodig: utf-8

import sys
import os
import traceback
import csv

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *


class ZCSVTableView(QTableView):
                
  def __init__(self, parent=None):
    super(QTableView, self).__init__()
        
    self.model = QStandardItemModel(parent)
    self.setModel(self.model)
    self.horizontalHeader().setStretchLastSection(True)
    self.model.setSortRole(Qt.UserRole)
 
    #parent.add(self)
    
    #self.load_file("../data/iris.csv")
    
    #self.show()

  
  def resizeToContents(self, columns):
    header = self.horizontalHeader()
    #header.setSectionResizeMode(0,   QHeaderView.Stretch)
    for i in range(columns):
      header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
  
  def strechLastSection(self, flag):
    self.horizontalHeader().setStretchLastSection(flag)

  def load_file(self, filename):
    # 1. Remove all rows from the self.model
    self.model.clear()

    # 2. Open CSV file and read lines and append those lines to the self.model.
    
    with open(filename) as f:
      reader = csv.reader(f)
      header = next(reader)                               
      self.model.setHorizontalHeaderLabels(header)

      for row in reader:
        items = []
        for column in row:
          items.append(QStandardItem(column))
        self.model.appendRow(items)


  def clear(self):
     # 1. Remove all rows from the self.model
     self.model.clear()

