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

# 2019/05/01

# ZEpochLogServer.py

import os
import sys
import time

import socketserver
import threading
import traceback

sys.path.append('../../')

from SOL4Py.ZMain  import *
from SOL4Py.network.ZThreadedUDPServer  import *

#=================================================
#
class ZEpochLogServer(ZThreadedUDPServer):

  ##
  # Constructor
  def __init__(self, ipaddress, port):
    ZThreadedUDPServer.__init__(self, ipaddress, port)
  
  # 
  def request_handle_callback(self, bytes, writer):
    print(__class__.__name__ + "::" + __class__.request_handle_callback.__name__ + " start")
    text = bytes.decode("utf-8")
    print(text)
    
    if "," in text:
      epoch, loss, acc, val_loss, val_acc = text.split(",")
  
      print("epoch:{} loss:{} acc:{} val_loss:{} val_acc:{}".format(epoch, loss, acc, val_loss, val_acc))
      # The values loss and acc may be plotted on figure of matplot. 


##################################################
#
#     
if main(__name__):
  ipaddress = "127.0.0.1"
  port      = 7777
  if len(sys.argv) >= 2:
    ipaddress = str(sys.argv[1])
  if len(sys.argv) >= 3:
    port = int(sys.argv[2])
    
  server = ZEpochLogServer(ipaddress, port)

  try:
    server.start()
    
    while True: 
      time.sleep(1)

  except (KeyboardInterrupt, SystemExit):
    print("Caught an exception")

  except:
    traceback.print_exc()

  else:
    pass

  finally:
    server.close()
    exit()
    