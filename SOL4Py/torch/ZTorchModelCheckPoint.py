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
 
# 2019/07/10

# ZTorchModelCheckPoint.py

# encodig: utf-8

import os
import sys

import traceback

sys.path.append('../')

from SOL4Py.ZMLModel import *
from SOL4Py.ZMain    import *
from SOL4Py.torch.ZTorchCallback    import *


class ZTorchModelCheckPoint(ZTorchCallback):
  ##
  # Constructor
  def __init__(self, dataset_id=0, save_starting_val_loss=0.3, 
                 save_fileformat="{id:02d}-{epoch:02d}-{train_loss:.2f}-{val_loss:.2f}.pt"):
    super(ZTorchModelCheckPoint, self).__init__()
    self.dataset_id = id
    self.monitor  = "val_loss"
    self.save_starting_val_loss = save_starting_val_loss
    self.save_filefomrat        = save_fileformat
    self.acc      = 0.0
    self.loss     = 0.0
    self.val_acc  = 0.0
    self.val_loss = 0.0
    pass


  def on_epoch_end(self, epoch, logs):
    if "," in logs:
      epoch, loss, acc, val_loss, val_acc = log.split(",")
      print("{} {} {} {}".format(loss, acc, val_loss, val_acc))
      self.acc      = float(acc)
      self.loss     = float(loss)
      self.val_acc  = float(val_acc)
      self.val_loss = float(val_loss)
      if self.val_loss < self.save_starting_val_loss:
         filename = self.save_fileformat.fomrat(self.dataset_id, epoch, self.loss, self.val_loss)
         print("Save file {}".format(filename))
         torch.save(net.state_dict(), save_filename)
         
   

