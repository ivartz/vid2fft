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
#    along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
#******************************************************************************/
 
#  ZTextureCoordTriangularBox.py

# encodig: utf-8

import numpy as np
import math
import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *


class ZTextureCoordTriangularBox(ZOpenGLObject):
  
  def __init__(self, x=1.0, y=1.0, z=1.0):
    super().__init__()
  
    #TextureCoord2Vertex3
    self.box  = [
        # Front
        # Face 0-1-2
        [[1.0, 1.0], [  x,  y, z]],
        [[0.0, 1.0], [ -x,  y, z]],
        [[0.0, 0.0], [ -x, -y, z]],
        # Face 2-3-0
        [[0.0, 0.0], [ -x, -y, z]],
        [[1.0, 0.0], [  x, -y, z]],
        [[1.0, 1.0], [  x,  y, z]],

        # Right
        # Face 0-3-4
        [[0.0, 1.0], [  x,  y,  z]],
        [[0.0, 0.0], [  x, -y,  z]],
        [[1.0, 0.0], [  x, -y, -z]],
        # Face 4-5-0
        [[1.0, 0.0], [  x, -y, -z]],
        [[1.0, 1.0], [  x,  y, -z]],
        [[0.0, 1.0], [  x,  y,  z]],

        # Top 
        # Face 0-5-6
        [[1.0, 0.0], [  x,  y,  z]],
        [[1.0, 1.0], [  x,  y, -z]],
        [[0.0, 1.0], [ -x,  y, -z]],
        # Face 6-1-0
        [[0.0, 1.0], [ -x,  y, -z]],
        [[0.0, 0.0], [ -x,  y,  z]],
        [[1.0, 0.0], [  x,  y,  z]],

        # Left
        # Face  1-6-7
        [[1.0, 1.0], [ -x,  y,  z]],
        [[0.0, 1.0], [ -x,  y, -z]],
        [[0.0, 0.0], [ -x, -y, -z]],
        # Face 7-2-1
        [[0.0, 0.0], [ -x, -y, -z]],
        [[1.0, 0.0], [ -x, -y,  z]],
        [[1.0, 1.0], [ -x,  y,  z]],

        # Bottom 
        # Face 7-4-3
        [[0.0, 0.0], [ -x, -y, -z]],
        [[1.0, 0.0], [  x, -y, -z]],
        [[1.0, 1.0], [  x, -y,  z]],
        # Face 3-2-7
        [[1.0, 1.0], [  x, -y,  z]],
        [[0.0, 1.0], [ -x, -y,  z]],
        [[0.0, 0.0], [ -x, -y, -z]],

        # Back
        # Face 4-7-6
        [[0.0, 0.0], [  x, -y, -z]],
        [[1.0, 0.0], [ -x, -y, -z]],
        [[1.0, 1.0], [ -x,  y, -z]],
        # Face 6-5-4
        [[1.0, 1.0], [ -x,  y, -z]],
        [[0.0, 1.0], [  x,  y, -z]],
        [[0.0, 0.0], [  x, -y, -z]]
    ]
    
    self.n_elements = len(self.box)
    self.n_faces    = 6
    self.n_vertices_per_face = 6


  def getBox(self):
    return self.box


  def getNumberOfElements(self):
    return self.n_elements


  def getNumberOfFaces(self):
    return self.n_faces
  
  
  def getNumberOfVerticesPerFace(self):
    return self.n_vertices_per_face
       
       