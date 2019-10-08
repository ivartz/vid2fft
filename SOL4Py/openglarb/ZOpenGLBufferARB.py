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
 
#  ZOpenGLBufferARB.py

# encodig: utf-8
import numpy as np
import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *
from OpenGL.GL.ARB.vertex_buffer_object import *

# http://oss.sgi.com/projects/ogl-sample/registry/ARB/vertex_buffer_object.txt


#ifdef GL_ARB_vertex_buffer_object

class ZOpenGLBufferARB(ZOpenGLObject):

  ## Constructor
  def __init__(self, target = GL_ARRAY_BUFFER_ARB):
    super().__init__()
    self.id     = 0
    self.target = target
    self.size   = 0
    self.id     = self.create(1)

    if self.id <=0:
      raise RuntimeError("Failed to create OpenGLBufferARB") 


  def create(self, size):
    return glGenBuffersARB(size)


  def destroy(self):  
    glDeleteBuffersARB(self.size, self.id)


  def bind(self): 
    glBindBufferARB(self.target, self.id)


  def unbind(self):
    glBindBufferARB(self.target, 0)


  def getBufferParameter(self, pname):
    return glGetBufferParameterivARB(self.target, pname)


  def getBufferPointer(self, pname):
    return glGetBufferPointervARB(self. target, pname)


  def data(self, sizei, data, usage=GL_DYNAMIC_DRAW_ARB):
    if sizei > 0 and data.all() != None:
      self.size = sizei
      glBufferDataARB(self.target, sizei, data, usage)


  def subData(self, offset, sizei, data):
    if offset > 0 and sizei > 0 and data != None: 
       glBufferSubDataARB(self.target, offset, sizei, data)



  def getBufferSubData(self, offset, size):
    return glGetBufferSubDataARB(self.target, offset, size)


  def isBuffer(self):
    return glIsBufferARB(self.id)


  def map(self, access):
    glMapBufferARB(self.target, access)


  def unmap(self):
    return glUnmapBufferARB(self.target)


#ifdef GL_ARB_draw_buffers

  def drawBuffers(self, n, bufs):
    self.bind()
    state = OpenGLClientState(GL_VERTEX_ARRAY)
    state.enable()

    glDrawBuffersARB(n, bufs) 

    state.disable()
    self.unbind()


#endif
  
  def drawArray(self, style):
    self.bind()
    
    state = OpenGLClientState(GL_VERTEX_ARRAY)
    state.enable()

    vertexNum = 3
    
    glVertexPointer(vertexNum, GL_FLOAT, 0, 0)
  
    dataNum = self.size / ( vertexNum * 4) # sizeof(GLfloat))
    print("dataNum %d\n", dataNum)
    
    glDrawArrays(style, 0 , dataNum)
    state.disable()
    
    self.unbind()



#endif

