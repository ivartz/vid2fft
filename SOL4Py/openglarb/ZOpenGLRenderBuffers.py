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
 
#  ZOpenGLRenderBuffers.py

# encodig: utf-8
import numpy as np
import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *
#from OpenGL.GL.ARB.render_buffer_object import *
from OpenGL.GL.ARB.vertex_buffer_object import *


class ZOpenGLRenderBuffers(ZOpenGLObject):

  def __init__(self, size, target=GL_RENDERBUFFER):
    self.size    = size
    self.target  = target
    self.buffers = None
    if size < 1:
      raise ValueError("Invalid parameters. size " + str(size))
    
    self.buffers = glGenRenderbuffers(self.size)


  def delete(self):
    glDeleteRenderbuffers(self.size, self.buffers)
  

  def bind(self, n=0):
    if self.size == 1:
      glBindRenderbuffer(self.target, self.buffers)
    elif n > 0 and n < self.size:
      glBindRenderbuffer(self.target, self.buffers[n])
    else:
      raise ValueError("Invalid index " + str(n)) ;

        
  def unbind(self):
    glBindRenderbuffer(self.target, 0)

 
  def get(self, n=0):
    if self.size == 1:
      return self.buffers
    elif n >0 and  n < size:
      return self.buffers[n] 
    else:
      raise ValueError("Invalid nth parameter " + str(n))


  def getParameteriv(pname):
    return glGetRenderbufferParameteriv(self.target, pname)


  def isRenderbuffer(self, buffer):
    return glIsRenderbuffer(buffer)


  def storage(self, internalformat, width, height):
    glRenderbufferStorage(self.target, internalformat, width, height)

#endif
  
  