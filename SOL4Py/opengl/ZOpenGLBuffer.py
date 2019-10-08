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
 
#  ZOpenGLBuffer.py

# encodig: utf-8

import numpy as np
from ctypes import *

from SOL4Py.opengl.ZOpenGLObject import *

class ZOpenGLBuffer(ZOpenGLObject) :
  
  def __init__(self, target=GL_ARRAY_BUFFER):
    super().__init__()
    
    self.id       = 0
    self.target   = target
    self.type     = GL_FLOAT
    self.byteSize = 0
    self.count    = 0
    self.stride   = 0
  
    self.id = glGenBuffers(1)


  def delete(self):
    glDeleteBuffers(1, self.id)

  def bind(self): 
    glBindBuffer(self.target, self.id)

  def unbind(self): 
    glBindBuffer(self.target, 0)

  def data(self, sizei, stride, count, data, usage=GL_DYNAMIC_DRAW):
      #if sizei > 0 and data.all() != None:
      self.byteSize = sizei
      self.stride   = stride
      self.count    = count
      glBufferData(self.target, self.byteSize, data, usage)

  def subData(self, offset, sizei, data):
    if offset > 0 and sizei > 0 and data.all() != None:
      glBufferSubData(self.target, offset, sizei, data)
  

  def drawArray(self, style):
    self.bind()
    glEnableClientState(GL_VERTEX_ARRAY)
    
    # Don't call glVertexPointer(self.stride, self.type, 0, 0)
    glVertexPointer(self.stride, self.type, 0, None)
    glDrawArrays(style, 0, self.count)

    glDisableClientState(GL_VERTEX_ARRAY)
    self.unbind()

  

