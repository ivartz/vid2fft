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
 
#  ZSingleton.py

# encoding utf-8

import sys
import os
import traceback

class ZSingleton:
  # class variable
  _singleton = None
  
  def set_instance(instance):
    if ZSingleton._singleton == None:
      ZSingleton._singleton = instance
    else:
      raise Exception("Already registered an instaance".format(ZSingleton._singleton))
   
  def get_instance():
    return ZSingleton._singleton
    
