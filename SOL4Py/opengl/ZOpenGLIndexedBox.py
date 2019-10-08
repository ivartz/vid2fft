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
 
#  ZOpenGLIndexedBox.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLQuadSurfaces import *
from SOL4Py.opengl.ZOpenGLIndexedVertices import *


class ZOpenGLIndexedBox(ZOpenGLIndexedVertices):

  STRIDE       = 3
  VERTEX_COUNT = 8
  FACE_COUNT   = 6
  
  ## Constructor  
  def __init__(self, w=1.0, h=1.0, d=1.0, x=0.0, y=0.0, z=0.0):
    super().__init__()

    self.vertices = [[0.0 for i in range(0, self.STRIDE)] for j in range(0, self.VERTEX_COUNT)]
    
    self.vertices[0] = [ float(0.0*w + x), float(0.0*h + y), float(0.0*d + z)  ]
    self.vertices[1] = [ float(1.0*w + x), float(0.0*h + y), float(0.0*d + z)  ]
    self.vertices[2] = [ float(1.0*w + x), float(1.0*h + y), float(0.0*d + z)  ]
    self.vertices[3] = [ float(0.0*w + x), float(1.0*h + y), float(0.0*d + z)  ]
    self.vertices[4] = [ float(0.0*w + x), float(0.0*h + y), float(-1.0*d + z) ]
    self.vertices[5] = [ float(1.0*w + x), float(0.0*h + y), float(-1.0*d + z) ]
    self.vertices[6] = [ float(1.0*w + x), float(1.0*h + y), float(-1.0*d + z) ]
    self.vertices[7] = [ float(0.0*w + x), float(1.0*h + y), float(-1.0*d + z) ]

    self.indices = [[0.0 for i in range(0, self.STRIDE)] for j in range(0, self.FACE_COUNT)]
    self.indices[0] = [0, 1, 2, 3]
    self.indices[1] = [1, 5, 6, 2]
    self.indices[2] = [5, 4, 7, 6]
    self.indices[3] = [4, 0, 3, 7]
    self.indices[4] = [4, 5, 1, 0]
    self.indices[5] = [3, 2, 6, 7]
       
    self.surfaces = ZOpenGLQuadSurfaces(self.vertices, self.indices)
    self.normals = self.surfaces.calculateSurfaceNormals()
    self.n_normals = len(self.normals)
    


  def getInterleavedArraysFormat(self):
    return 0  #unused
  
  
  def getPrimitiveType(self):
    return GL_QUADS
  
  
  def getVertices(self):
    return self.vertices  # unused
  
  
  def getVerticesDataSize(self):
    return len(self.vertices)
  

  def getNumberOfVertices(self):
    return len(self.vertices)
  
  
  def getIndices(self):
    return self.indices #unused
  
  
  def getIndicesDataSize(self):
    return len(self.lindices)
  
  
  def getNumberOfIndices(self):
    return len(self.indices)
  
  
  def draw(self):
    glFrontFace(GL_CCW)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)
    glEnable(GL_NORMALIZE)
        
    for i in range(len(self.indices)): 
      glBegin(GL_QUADS)
      glNormal3fv( self.normals[i] )
      quad = self.indices[i]
      
      glVertex3fv( self.vertices[ quad[0] ] ) 
      glVertex3fv( self.vertices[ quad[1] ] )
      glVertex3fv( self.vertices[ quad[2] ] )
      glVertex3fv( self.vertices[ quad[3] ] )
      
      glEnd()
   