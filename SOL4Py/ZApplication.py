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
 
#  ZApplication.py

# encodig: utf-8

import sys
import os
import traceback
from time import sleep

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from SOL4Py.ZApplicationView import *

#---------------------------------------------------------------------

class ZApplication(QApplication):
  
  def __init__(self, argv):
    super(ZApplication, self).__init__(argv)
   
  
  def run(self, view, interval= 0.001):
    # Check sleep interval
    if interval < 0.0001 or interval >1.0:
      interval = 0.001
      
    if isinstance(view, ZApplicationView):
      while True:
        QApplication.processEvents()
        sleep(interval)      
        view.render()
        if view.is_terminated():
          break
    else:
      print("Invalid view parameter")    

  def exec(self, interval= 0.001):
    # Check sleep interval
    if interval < 0.0001 or interval >1.0:
      interval = 0.001
      
    while True:
        QApplication.processEvents()
        sleep(interval)      
       # if view.is_terminated():
       #   break


def main(name):    
  if name == '__main__':
    return True
  else:
    return False

      
