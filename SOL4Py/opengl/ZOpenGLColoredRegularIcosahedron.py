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
 
#  ZOpenGLColoredRegularIcosahedron.py

# Icosahedron's vertices data used here is based on the following webstie 
#
# https://en.wikipedia.org/wiki/Platonic_solid

# encodig: utf-8

import numpy as np
import math

from ctypes import *

from SOL4Py.opengl.ZOpenGLIndexedVertices import *

  
class ZOpenGLColoredRegularIcosahedron(ZOpenGLIndexedVertices):

  STRIDE   = 6;
  FACES    = 20;
  VERTICES = 12;


  ## Constructor  
  def __init__(self, colors=None, numColors=0):
    super().__init__()
    
    self.vertices         = None
    self.verticesDataSize = 0
    self.indices          = None
    self.indicesDataSize  = 0
     
    g = (1.0 + math.sqrt(5.0))/2.0; #golden ratio

    self.vertices = [
      # R,  G,  B,     X,    Y,    Z
      # 12 vertices
      1.0, 0.0, 0.0,   0.0, -1.0, -g  ,
      1.0, 0.2, 0.2,   0.0, +1.0, -g  ,
      1.0, 0.4, 0.4,   0.0, -1.0, +g  ,
      1.0, 0.6, 0.6,   0.0, +1.0, +g  ,
      
      0.8, 0.8, 0.6,  -g,    0.0, -1.0,
      0.8, 1.0, 0.6,  -g,    0.0, +1.0,
      0.6, 0.8, 1.0,  +g,    0.0, -1.0,
      0.4, 0.6, 1.0,  +g,    0.0, +1.0,
      
      0.2, 0.4, 1.0,  -1.0, -g,    0.0,
      0.0, 0.2, 1.0,  +1.0, -g,    0.0,
      0.2, 0.0, 0.8,  -1.0, +g,    0.0, 
      0.4, 0.2, 0.6,  +1.0, +g,    0.0,
      ]

    self.verticesDataSize = len(self.vertices) * 4
    self.numberOfVertices = len(self.vertices);

    if colors != None and numColors == self.VERTICES:
      self.setVerticesColors(colors, numColors);
    
    self.indices = [    
     #20 faces
     0,  1,  6,
     1,  0,  4,
     2,  3,  5,
     3,  2,  7,
     4,  5, 10,
     5,  4,  8,
     6,  7,  9,
     7,  6, 11,
     8,  9,  2,
     9,  8,  0, 
    10, 11,  1,
    11, 10,  3,
      
     0,  6,  9,
     0,  8,  4, 
     1,  4, 10,
     1, 11,  6,
     2,  5,  8,
     2,  9,  7, 
     3,  7, 11,
     3, 10,  5
    ]
    
    self.indicesDataSize = len(self.indices) * 4;
    
    self.numberOfIndices = len(self.indices);



  def setVerticesColors(self, colors, numColors):
    if colors != None and numColors == self.VERTICES:
      for i in range(numColors):
        self.vertices[i * self.STRIDE + 0] = colors[i][0];
        self.vertices[i * self.STRIDE + 1] = colors[i][1];
        self.vertices[i * self.STRIDE + 2] = colors[i][2];


  def getInterleavedArraysFormat(self):
    return GL_C3F_V3F;


  def getPrimitiveType(self):
    return GL_TRIANGLES;


  def getVertices(self):
    return self.vertices;


  def getVerticesDataSize(self):
    return self.verticesDataSize;


  def getNumberOfVertices(self):
    return self.numberOfVertices;


  def getIndices(self):
    return self.indices;


  def getIndicesDataSize(self):
    return self.indicesDataSize;


  def getNumberOfIndices(self):
    return self.numberOfIndices;


  def draw(self):
    glFrontFace(GL_CCW);
    glEnable(GL_CULL_FACE);
    glCullFace(GL_BACK);
    glInterleavedArrays(self.getInterleavedArraysFormat(), 0, None);
    glDrawElements(self.getPrimitiveType(), self.getNumberOfIndices(), GL_UNSIGNED_INT, None);

  