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
 
#  ZOpenGLTimerThread.py

# encodig: utf-8

import sys
import os
import math
import traceback
import time
import threading

import numpy as np

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal

 
class ZOpenGLTimerThread(QThread):

  # ZOpenGLTimerThread Constructor
  def __init__(self, opengl_view, interval = 200):  #200msec
    QThread.__init__(self)
    if opengl_view == None:
      raise ValueError("ZOpenGLTimerThread: opengl_view is None")
       
    self.opengl_view = opengl_view
    self.rendering_interval = interval/1000
    self.looping = True


  def terminate(self):
    self.looping = False


  def run(self):
    while self.looping == True:
      time.sleep(self.rendering_interval)
      self.opengl_view.update()

