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
#    but WITHOUT ANY WARRANTY without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/
 
#  ZTextureCoord2Vertex3.py

# encodig: utf-8

from SOL4Py.ZVector2 import *
from SOL4Py.ZVector3 import *

class ZTextureCoord2Vertex3:
 
  def __init__(self, coord2, vertex3):
    self.coord2  = ZVector2(coord2)
    self.vertex3 = ZVector3(vertex3)
    



