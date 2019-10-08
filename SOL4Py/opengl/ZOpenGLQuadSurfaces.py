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

#2016/09/10 On calculateSurfaceNormals method, see: https://www.opengl.org/wiki/Calculating_a_Surface_Normal
 
#  ZOpenGLQuadSurfaces.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLQuadSurfaces:

  ## Constructor
  def __init__(self, vertices, faces):
    self.vertices   = vertices   # list of vertex = [x, y, z]
    self.n_vertices = len(self.vertices)
    self.faces      = faces
    self.n_faces   = len(self.faces)
    self.normals    = None
    self.n_normals  = 0


  def calculateSurfaceNormals(self):

    self.n_normals = self.n_faces;
    self.STRIDE  = 3
    
    self.normals = [[0.0 for i in range(0, self.STRIDE)] for j in range(0, self.n_faces)]
    
    for s in range(self.n_faces):
      quad = self.faces[s];

      v = [
        self.vertices[ quad[0] ],
        self.vertices[ quad[1] ],
        self.vertices[ quad[2] ],
        self.vertices[ quad[3] ]
      ]
      
      normal = [0, 0, 0]
      
      for i  in range(self.STRIDE+1):
        j = (i+1) % (self.STRIDE+1);
        normal[0] += (v[i][1] - v[j][1]) * (v[i][2] + v[j][2]);
        normal[1] += (v[i][2] - v[j][2]) * (v[i][0] + v[j][0]);
        normal[2] += (v[i][0] - v[j][0]) * (v[i][1] + v[j][1]);
      
      normal = self.normalize(normal);
        
      self.normals[s][0] = normal[0];
      self.normals[s][1] = normal[1];
      self.normals[s][2] = normal[2];
   
    self.n_normals = len(self.normals)
    return self.normals
    

  def normalize(self, v):
    sq = 0
    for i in range(len(v)):
      sq += v[i]*v[i]
    length = math.sqrt(sq)
    
    for i in range(len(v)):
      v[i] = v[i] /length
    
    return v

    