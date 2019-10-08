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
 
#  ZOpenGLBufferedShape.py

# encodig: utf-8



from SOL4Py.opengl.ZOpenGLIndexedVertices  import *   
from SOL4Py.openglarb.ZOpenGLVertexBufferARB  import *
from SOL4Py.openglarb.ZOpenGLIndexBufferARB  import *
from SOL4Py.opengl.ZOpenGLMateria  import *

class ZOpenGLBufferedShape(ZOpenGLObject):
  ## Constructor  

  def __init__(self, vertices, materia=None):
    super().__init__()
 
    self.vertices = vertices
    self.materia  = materia
    if vertices != None:
      self.vertexBuffer = ZOpenGLVertexBufferARB();
      self.vertexBuffer.bind();
      ver = np.array(vertices.getVertices(), dtype="float32")
      
      self.vertexBuffer.data(vertices.getVerticesDataSize(), ver, GL_STATIC_DRAW_ARB);
      self.vertexBuffer.unbind();
              
      self.indexBuffer = ZOpenGLIndexBufferARB();
      self.indexBuffer.bind();
      ind = np.array(vertices.getIndices(), dtype="int")
      self.indexBuffer.data(vertices.getIndicesDataSize(), ind, GL_STATIC_DRAW_ARB);
      self.indexBuffer.unbind();
    else:
      raise ValueError("Invalid vertices parameter.");


  def draw(self): 
    self.vertexBuffer.bind();
    self.indexBuffer.bind();
    if self.materia != None:
      self.materia.materialize();
    self.vertices. draw();
   
    self.vertexBuffer.unbind();
    self.indexBuffer.unbind();

