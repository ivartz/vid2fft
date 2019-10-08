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
 
#  ZOpenGLSolidTorus.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLGeometry import *


class ZOpenGLSolidTorus(ZOpenGLGeometry):

  def __init__(self, materia, inner, outer, sides, rings):
    super().__init__(materia)
    
    self.reshape(inner, outer, sides, rings)
    
  def reshape(self, inner, outer, sides, rings):
    self.innerRadius = inner
    self.outerRadius = outer
    self.sides       = sides
    self.rings       = rings

  
  def draw(self, x=0.0, y=0.0, z=0.0):
    glPushMatrix()
    self.materialize()
    self.solidTorus(self.innerRadius, self.outerRadius, self.sides, self.rings)
    
    glPopMatrix()

  
