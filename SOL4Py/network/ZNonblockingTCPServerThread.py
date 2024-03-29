﻿#/******************************************************************************
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

# 2018/09/30

# Simple Nonblocking TCP Socket Server thread example
# ZNonblockingTCPServerThread.py


# encoding: utf-8

import os
import sys
import traceback
import socket
import threading
import time

from SOL4Py.network.ZClientRequestHandlerThread import *


##
#
# Nonblocking TCP Socket Server thread
#
class ZNonblockingTCPServerThread(threading.Thread):

  ##--------------------------------------------------------
  # Inner class starts.
  # Inner thread class to handle a communication with a client 
  
  class ClientRequestHandlerThread(ZClientRequestHandlerThread):
    ## 
    # Construcotr
    def __init__(self, client_sock, address, server_sock):
      super(ZNonblockingTCPServerThread.ClientRequestHandlerThread, self).__init__(client_sock, address, server_sock)

  ## Inner class ends.
  ##--------------------------------------------------------
 
  # Class variables
  BACK_LOG = 128
   

  ##
  # Constructor
  
  def __init__(self, host, port):
    super(ZNonblockingTCPServerThread, self).__init__()

    self.host = host
    self.port = port
    
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind((self.host, self.port))
    self.sock.setblocking(False)
    self.sock.listen(ZNonblockingTCPServerThread.BACK_LOG)
    
    self.looping = True
    self.sleep_interval = 0.01

  # Please define your own create_request_handler_thread in a subclass derived from this class  
  def create_request_handler_thread(self, client, address, server_sock):
    thread = ZNonblockingTCPServerThread.ClientRequestHandlerThread(client, address, self.sock)
    thread.start()
  
  
  def run(self):
    print("run::start")
    self.looping = True
    
    while True:
      try:
        time.sleep(self.sleep_interval)
        if self.looping == False:
          break
        
        if self.sock != None:
          client, address = self.sock.accept()
          self.create_request_handler_thread(client, address, self.sock)
        else:
          break

      except (BlockingIOError, socket.error):
        continue

      except (KeyboardInterrupt, SystemExit):
        print("Caught an exception")
        break
        
      except:
        traceback.print_exc()
        break

  def stop(self):
     print("Stop server thread")
     #self.sock.close()
     self.sock = None
     self.looping = False


