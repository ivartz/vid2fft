#/******************************************************************************
# 
# Copyright (c) 2018 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/
 
# ZClientRequestHandlerThread.py

# encoding:utf-8


import sys
import os
import traceback
import socket
import threading
import time

class ZClientRequestHandlerThread(threading.Thread):
  DATA_ENCODER   = "utf-8"
  BUF_SIZE       = 1024*8
  SLEEP_INTERVAL = 0.01
  
  
  ## 
  # Construcotr
  def __init__(self, client, address, server_sock):
   super(ZClientRequestHandlerThread, self).__init__()

   self.client = client
   self.address = address
   self.server_sock = server_sock
   self.looping = True 
   self.reply  = "OK"
   if ZClientRequestHandlerThread.DATA_ENCODER != None:
     self.reply = self.reply.encode(ZClientRequestHandlerThread.DATA_ENCODER)
     

   
  # Default client request handler
  # Please redefine handle_request method in a subclass derived from this class.
  #
  def handle_request(self, data):
    if ZClientRequestHandlerThread.DATA_ENCODER != None:
      data = data.decode(ZClientRequestHandlerThread.DATA_ENCODER)
    
    # Print the received data.  
    print("Recv:{}".format(data))
    
    # Send self.reply to self.client.
    self.client.send(self.reply)


  # Thread main procedure, which can be called by thread.start()
  def run(self):
    print("Thread run:: start") 
    print("Connected from: {} {}".format(self.client, self.address))

    while self.looping:
      try:
        time.sleep(ZClientRequestHandlerThread.SLEEP_INTERVAL)
        data = self.client.recv(ZClientRequestHandlerThread.BUF_SIZE)
        if len(data):
          self.handle_request(data)
        else:
          raise Exception("Disconnected from: {} {}".format(self.client, self.address))

      except (BlockingIOError, socket.error):
        continue

      except (KeyboardInterrupt, SystemExit):
        print("Caught KeyboardIntrrupt exception")
        break
 
      except:
        traceback.print_exc()
        break
    
    self.stop()


  def stop(self):
    try:
    
      self.client.shutdown(socket.SHUT_RDWR)
      self.client.close()
    except:
      pass
