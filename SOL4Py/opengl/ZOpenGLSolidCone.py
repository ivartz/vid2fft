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
 
#  ZOpenGLSolidCone.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLGeometry import *

class ZOpenGLSolidCone(ZOpenGLGeometry):
  
  def __init__(self, materia, base, height, slices, stacks):
    super().__init__(materia)
    
    self.reshape(base, height, slices, stacks)
  
  def reshape(self, base, height, slices, stacks):
    
    self.base   = base
    self.height = height
    self.slices = slices
    self.stacks = stacks
    
  def draw(self): #, x, y, z):
    glPushMatrix()
    #glTranslate(x, y, z)
    self.materialize()
    self.solidCone(self.base, self.height, self.slices, self.stacks)
    glPopMatrix()

