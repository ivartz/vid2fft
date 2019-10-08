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


#  ZOpenGLVertexArrays.py

# encodig: utf-8


from SOL4Py.opengl.ZOpenGLObject import *
from OpenGL.GL.ARB.vertex_array_object import *


#ifdef GL_ARB_vertex_array_object

class ZOpenGLVertexArrays(ZOpenGLObject):
  
  def __init__(self, size):
    super().__init__(1)
    self.size = size
    self.buffer = glGenVertexArrays(self.size)


  def delete(self):
    glDeleteVertexArrays(self.size, self.buffer);


  def getNth(self, i):
    if i >= 0 and i < size:
      return self.ids[i];
    else:
      raise ValueError("Invalid argument " + str(i)); 
  
  def getSize(self):
    return self.size;
 
  
  def bindNth(self, n):
    if n >= 0 and n < size:
      glBindVertexArray(self.ids[n]);
    else:
      raise ValueError("Invalid argument " + str(n)); 
 

  def unbind(self):
    glBindVertexArray(0);

  def isVertexArray(self, n):
    return glIsVertexArray(n);
 

#endif

