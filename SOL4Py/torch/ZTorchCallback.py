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
 
# 2019/06/25

# ZTorchCallback.py

# encodig: utf-8

import os
import sys

import traceback

sys.path.append('../')

from SOL4Py.ZMLModel import *
from SOL4Py.ZMain    import *

# This is a abstract ZTorchCallback class.

class ZTorchCallback:
  ##
  # Constructor
  def __init__(self):
    pass

  ## 
  # Destructor
  def __del__(self):
    print("ZTorchCallback.Destructor")


  def on_train_begin(self, logs={}):
    pass


  def on_epoch_end(self, epoch, logs):
    pass


