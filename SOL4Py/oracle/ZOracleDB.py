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

# OracleDB.py

# 2018/09/30

# encoding: utf-8

import sys
import os
import configparser

import cx_Oracle

class ZOracleDB:

  def __init__(self, user=None, passwd=None, service=None, server='localhost', port='1521', argv=None):
    self.user = user
    self.passwd = passwd
    self.service = service
    self.server  = server
    self.port    = port
    self.cursor  = None
    self.connection = None
    if argv != None:
      if len(sys.argv) <=3:
        raise Exception("Usage: {} user passwd service [server port]")
        
      self.user    = sys.argv[1]
      self.passwd  = sys.argv[2]
      self.service = sys.argv[3]
      self.server  = 'localhost'
      self.port    = '1521'
    
    if len(sys.argv) > 4:
      self.server = sys.argv[4]
      
    if len(sys.argv) > 5:
      self.port   = sys.argv[5]

    self.connect()
    
  def connect(self):
    try:
      self.connection = cx_Oracle.connect(self.user, self.passwd, 
                     self.server + ':' + self.port + '/' + self.service )
      self.cursor = self.connection.cursor()

    except (cx_Oracle.DatabaseError) as ex:
      print(ex)
      raise ex

  def query(self, sql):
    try:
       self.cursor.execute(sql)
       rows = self.cursor.fetchall()
       return rows

    except (cx_Oracle.DatabaseError) as ex:
       print(ex)
       raise ex

  def execute(self, sql):
    try:
       self.cursor.execute(sql)

    except (cx_Oracle.DatabaseError) as ex:
       print(ex)
       raise ex


  def get_connection(self):
    return self.connection


  def get_cursor(self):
    return self.cursor


  