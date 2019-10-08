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

# ZEpochChangeNotifier.py

# encodig: utf-8

import os
import sys
import socket

import traceback



sys.path.append('../')

from SOL4Py.ZMLModel import *
from SOL4Py.ZMain    import *
from SOL4Py.torch.ZTorchCallback    import *

# This class will send a text messge to notify a progress status of traing proccess
# of this Model class to a notificant. The text message will be sent the notificant 
# by using a datagram socket.
# This is a subclass derived from ZTorchCallback keras.callback

class ZTorchEpochChangeNotifier(ZTorchCallback):
  ##
  # Constructor
  def __init__(self, ipaddress, port, notifier="", epochs=100):
    super(ZTorchEpochChangeNotifier, self).__init__()

    self.sock     = None
    self.notifier = notifier
    self.epochs   = epochs

    # Create a DATGRAM socket
    try:
      self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      self.server_address = (ipaddress, port)
      print(self.server_address)
    except:
      print(formatted_traceback())


  ## 
  # Destructor
  def __del__(self):
    print("ZEpochChangeNotifier.Destructor")
    self.close()


  def on_train_begin(self, logs={}):
    print("on_train_begin")
    self.send("on_train_begin:" + self.notifier + ":" + str(self.epochs) )


  def send(self, message):
    text = str(message)
    # You should send a "utf-8" encoded data
    data = text.encode("utf-8")
    self.sock.sendto(data, self.server_address)


  def on_epoch_end(self, epoch, logs):
    print("on_epoch_end :epoch:{}".format(epoch))

    acc     = 0
    if 'acc' in logs:
      acc      = logs.get('acc')
    val_acc = 0
    if 'val_acc' in logs:
      val_acc  = logs.get('val_acc')
    loss     = logs.get('loss')
    val_loss = logs.get('val_loss')
    
    message = "{}, {:.4f}, {:.4f}, {:.4f}, {:.4f}".format(epoch, loss, acc, val_loss, val_acc)
    # Send (epoch, loss, acc, val_loss, val_acc) to a UDP server
    self.send(message)


  def close(self):
    if self.sock != None:
      self.sock.close()
      self.sock = None


