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
 
#  ZTableView.py

# encodig: utf-8

import sys
import os
import traceback
import csv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#---------------------------------------------------------------------

class ZTableView(QWidget):

  def __init__(self, parent):
    super(ZTableView, self).__init__(parent)
    self.model = QStandardItemModel(self)

    self.tableView = QTableView(self)
    self.tableView.setModel(self.model)
    self.tableView.horizontalHeader().setStretchLastSection(True)
    self.tableView.verticalHeader().setStretchLastSection(True)
    self.tableView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
   
    self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
    self.tableView.resizeColumnsToContents()
        
  def load_csv(self, filename):

    with open(filename, "r") as file:
      for row in csv.reader(file):
        items = [
                 QStandardItem(field)
                 for field in row
        ]
        self.model.appendRow(items)
    self.tableView.resizeRowsToContents()
    self.tableView.resizeColumnsToContents()

  def resize(self, event):
    self.tableView.resizeRowsToContents()
    self.tableView.resizeColumnsToContents()

  def disable_edit(self):
    self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


