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

# ZThreadedTCPServer.py

# encoding utf-8

# Simple TCPServer example to accept single TCPClien
# See https://docs.python.org/3/library/socketserver.html
# See also: https://gist.github.com/arthurafarias/7258a2b83433dfda013f1954aaecd50a#file-server-py

import os
import sys
import time

import socketserver
import threading
import traceback

from SOL4Py.ZSingleton import *

##
# Simple TCPServer thread class, which handles a stream request from a TCP client.
#
class ZThreadedTCPServer(threading.Thread, ZSingleton):

  #---------------------------------------------------------
  # Inner class starts. 
  # Define your subclass derived from StreanRequestHandler
  class _TCPRequestHandler(socketserver.StreamRequestHandler):
      
    # Define your own handle method if needed.
    def handle(self):     
      print(self.__class__.__name__ + self.handle.__name__ + " start")
      print("Curent thread name:{}".format(threading.current_thread().name))
      try:
        
        while True:
          print("Curent thread name:{}".format(threading.current_thread().name))
          bytes = self.rfile.readline().strip()
          if len(bytes) == 0:
            print("breaking handle loop")
            break
          
          ZSingleton.get_instance().request_handle_callback(bytes, self.wfile)
            
        self.request.close()

      except:
        traceback.print_exc()
      
  # Inner class ends.
 
 
  ##
  #
  # Constructor
  def __init__(self, ipaddress, port, request_handler_class = None):
    super(ZThreadedTCPServer, self).__init__()
    
    print(self.__class__.__name__ + "::" + self.run.__name__ + " start")

    ZSingleton.set_instance(self)
    
    print("IPAddress:{} Port:{}".format(ipaddress, port))
    self.server_address = (ipaddress, port)
    
    if request_handler_class == None:
      # Register the default request handler class: self._TCPRequestHandler.
      self.sock_server = socketserver.TCPServer(self.server_address, self._TCPRequestHandler)
    else:
      self.sock_server = socketserver.TCPServer(self.server_address, request_handler_class)
    
    self.sock_server.allow_reuse_address = True

  
  # Please redefine your own method 'request_handle_callback' in a subclass derived from this class.
  def request_handle_callback(self, bytes, writer):
    text = bytes.decode("utf-8")
    import datetime
    now = datetime.datetime.now()
    print("Recieved at {} data :{}".format(now, text)) 
    reply  = "OK"
    breply = reply.encode("utf-8")
    writer.write(breply)


  # Thread main procedure.
  def run(self):
    print(self.__class__.__name__ + "::" + self.run.__name__ + " start")
    if self.sock_server != None:
      self.sock_server.serve_forever()    
    print(self.__class__.__name__ + "::" + self.run.__name__ + " end")


  # Shdown and close server_socket.
  def close(self):
    if self.sock_server != None:
      self.sock_server.shutdown() 
      print("sock_server shutdown")
       
      self.sock_server.server_close()
      print("sock_server close")
