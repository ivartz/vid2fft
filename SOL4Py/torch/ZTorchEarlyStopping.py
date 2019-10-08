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
from SOL4Py.torch.ZTorchCallback    import *


class ZTorchEarlyStopping(ZTorchCallback):
  ##
  # Constructor
  def __init__(self, monitor="val_loss", mode="min"):
    super(ZTorchEpochChangeNotifier, self).__init__()
    self.monitor  = monitor
    self.mode     = mode
    
    self.acc      = 0.0
    self.loss     = 0.0
    self.val_acc  = 0.0
    self.val_loss = 0.0
    pass


  def on_epoch_end(self, epoch, logs):
    rc = False
    if "," in logs:
      epoch, loss, acc, val_loss, val_acc = log.split(",")
      print("{} {} {} {}".format(loss, acc, val_loss, val_acc))
      prev_acc      = self.acc
      prev_loss     = self.loss
      prev_val_acc  = self.val_acc
      prev_val_loss = self.val_loss
      
      self.acc      = float(acc)
      self.loss     = float(loss)
      self.val_acc  = float(val_acc)
      self.val_loss = float(val_loss)
      # TO DO 
      # implementation
    
    return rc


