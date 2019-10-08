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
 
#  ZMain.py

import sys
import os
import traceback

def main(name):    
  if name == '__main__':
    return True
  else:
    return False

def formatted_traceback():
   return traceback.format_exc()


if main(__name__):
  try:
    node = Node()
    node.write()

  except Exception as ex:
     print("#Caught:Exception: {0}".format(ex))
  except:
    print("#Caught:" + formatted_traceback())
    
