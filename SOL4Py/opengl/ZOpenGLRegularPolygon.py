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
 
#  ZOpenGLRegularPolygon.py

# encodig: utf-8

import numpy as np
import math
#import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl.ZOpenGLQuadric import *


class ZOpenGLRegularPolygon(ZOpenGLObject):
  ## Constructor
  def __init__(self, number, primitive=GL_TRIANGLE_FAN, z=0.0):
    super().__init__()
    
    self.number    = number
    self.primitive = primitive
    self.polygon   = [[0.0 for i in range(3)] for j in range(self.number+1)]
     
  
    delta = 2.0 * math.pi / float(self.number);
    for i in range(self.number+1):
      self.polygon[i][0] = math.cos(delta * i);
      self.polygon[i][1] = math.sin(delta * i);
      self.polygon[i][2] = z; 
  
  def draw(self):
    glBegin(self.primitive);
    
    if self.primitive == GL_TRIANGLE_FAN:
      glVertex3f(0.0, 0.0, 0.0);
  
    for i in range(self.number+1):
      glVertex3fv(self.polygon[i]) #.[0], polygon[i].y, polygon[i].z);
    
    glEnd();


