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
 
#  ZLabeledFileComboBox.py

# encoding: utf-8

import sys
import os
import glob
import traceback

from PyQt5 import QtCore, QtWidgets, QtGui

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *

from SOL4Py.ZLabeledComboBox import *
 
# This is a special combobox to display file names matched with a file pattern
# somthing like a C:\data\images\*.png.

# This also have a push button to show a folder selection dialog.

class ZLabeledFileComboBox(ZLabeledComboBox):
  
  # Contructor
  
  def __init__(self, parent, label="LabeledFileComboBox", orientation=Qt.Horizontal):
    ZLabeledComboBox.__init__(self, parent, label, orientation)
    # Create an instance of QPushButton and add it to the layout of this combobox
    self.folder_button = QPushButton("...", self)
    self.add(self.folder_button)


  # Register a button clicked callback to the self.folder_button.  
  def add_clicked_callback(self, clicked_callback):
    self.folder_button.clicked.connect(clicked_callback)    

  # List up all files matched with a file_pattern.
  # If filenames_only was True, this combobox displays filenames, 
  # if not, full path names.
  def listup_files(self, file_pattern, filename_only=True):
    abspath = os.path.abspath(file_pattern)
    slashed = abspath.replace(os.path.sep, '/')
    self.dir, _ = os.path.split(slashed)

    files = sorted(glob.glob(slashed))
      
    self.set_label(self.dir)

    if files != None:
      self.get_combobox().clear()
      self.set_size_adjust_policy()
      
      for file in files:
        # split file into dir and name.
        if filename_only == True:
          _, name = os.path.split(file)
          self.add_item(name)
        else:
          self.add_item(filename)

  def get_current_text_as_fullpath(self):
    current_text = self.get_current_text()
    #dirname = os.path.dirname(self.dir)
    #print("Dirname {} filename {}".format(self.dir, current_text) )
    path = os.path.join(self.dir, current_text)
    slashed_path = path.replace(os.path.sep, '/')
    return slashed_path
