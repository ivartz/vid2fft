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
 
#  ZOpenGLBitmap.py

# encodig: utf-8

from SOL4Py.ZColor4 import *
from SOL4Py.opengl.ZOpenGLObject import *

class ZOpenGLBitmap(ZOpenGLObject):
  ## Constructor
  def __init__(self, x, y, width, height, 
                    depth, format=GL_RGB, type = GL_UNSIGNED_BYTE):
    super().__init__()
    
    self.x        = x
    self.y        = y
    self.width    = width
    self.height   = height
    self.format   = format
    self.type     = type
    self.channels = 0
    self.depth    = depth
  
    self.channels = 1
    if self.format == GL_RGB:
      self.channels = 3
    elif self.format == GL_RGBA:
      self.channels = 4
    else:
      self.channels = 1


  def readPixels(self, buffer=GL_BACK):
    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    glReadBuffer(buffer)
    return glReadPixels(self.x, self.y, self.width, self.height, self.format, self.type)
 


