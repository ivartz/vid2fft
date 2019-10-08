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
 
#  ZPlottingArea.py

# encodig: utf-8

import sys
import signal
import numpy as np
import traceback
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

from numpy.random import rand


from PyQt5 import QtCore, QtWidgets, QtGui

from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *


matplotlib.use("Qt5Agg")

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class ZPlottingArea(FigureCanvas):

  # Constructor  
  def __init__(self, parent, width, height, figure=None):
    dpi = 80
    w = width /dpi
    h = height/dpi
    if figure is None:
      self.figure = plt.figure(figsize=(w, h), dpi=dpi)
    else:
      self.figure = figure
    self.figure.tight_layout()

    super(ZPlottingArea, self).__init__(self.figure)
    self.setParent(parent)

    self.show()

  def add(self, index):
    return self.figure.add_subplot(index)

  def add_subplot(self, x, y, i):
    plt.subplot(x, y, i)

  def get_figure(self):
    return self.figure
    
  def set_figure(self, fig):
    try:
      if self.figure is not None:
        plt.close(self.figure)
      self.figure = fig
    except:
      pass
 
  def close(self):
    if self.figure is not None:
      plt.close(self.figure)
      self.figure = None


  def clear(self):
    if self.figure is not None:
      #self.figure.cla()
      plt.cla()    
