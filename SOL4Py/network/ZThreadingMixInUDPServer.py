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

# 2018/09/20

# ZThreadingMixInUDPServer.py

# encoding utf-8

# Simple UDPServer example to accept single UDPClien
# See https://docs.python.org/3/library/socketserver.html
# See also: https://gist.github.com/arthurafarias/7258a2b83433dfda013f1954aaecd50a#file-server-py

import os
import sys
import time

import socketserver
import threading
import traceback

from SOL4Py.ZSingleton import *

##################################################
#
class ZThreadingMixInUDPServer(ZSingleton):
  
  # Inner classes start.
  # Default RequestHandler
  class _UDPRequestHandler(socketserver.DatagramRequestHandler):

    def handle(self):
      print(self.__class__.__name__ + self.handle.__name__ + " start")
      print("Curent thread name:{}".format(threading.current_thread().name))
      try:
        while True:
          bytes = self.rfile.readline().strip() 
          if len(bytes) == 0:
            break
          ZSingleton.get_instance().request_handle_callback(bytes, self.wfile)

      except:
        traceback.print_exc()

  # Inner class
  class _ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass
 
  # Inner classes end.
  
 
  ##
  # Constructor
   
  def __init__(self, ipaddress, port, request_handler_class=None):
    self.ipaddres      = ipaddress
    self.port          = port

    ZSingleton.set_instance(self)
    
    if request_handler_class == None:
      # Register the default request handler.
      self.server        = self._ThreadedUDPServer((ipaddress, port), 
                                  self._UDPRequestHandler)
    else:
      self.server        = self._ThreadedUDPServer((ipaddress, port), 
                                  request_handler_class)
                                  
    self.server.allow_reuse_address = True
 
    self.server_thread = threading.Thread(target=self.server.serve_forever)
    self.server_thread.daemon = True


  # Please redefine your own method 'request_handle_callback' in a subclass derived from this class.
  def request_handle_callback(self, bytes, writer):
    text = bytes.decode("utf-8")
    import datetime
    now = datetime.datetime.now()
    print("Recieved at {} data :{}".format(now, text)) 
    reply  = "OK"
    breply = reply.encode("utf-8")
    writer.write(breply)


  def start(self):
    print(self.__class__.__name__ + "::" + self.start.__name__ + "start")
    self.server_thread.start()


  def close(self):
    self.server.shutdown()
    print("sever shutdown")
    self.server.server_close()
    print("server close")

