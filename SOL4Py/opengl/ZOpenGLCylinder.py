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
 
#  ZOpenGLCylinder.py

# encodig: utf-8

import sys

# 

from SOL4Py.opengl.ZOpenGLShape import *


class ZOpenGLCylinder(ZOpenGLShape):
  
  def __init__(self, quadric, materia, base=1.0, top=1.0, height=1.0, slices=40, stacks=40):
    super().__init__(quadric, materia)
    self.reshape(base, top, height, slices, stacks)


  def reshape(self, base, top, height, slices, stacks):
    self.base   = base  
    self.top    = top
    self.height = height
    self.slices = slices
    self.stacks = stacks


  def draw(self):  
    gluCylinder(self.getQuadric(),
          self.base,
          self.top,  
          self.height, 
          self.slices,  
          self.stacks)


  def translate(self, x, y, z):  
      glPushMatrix()
      glTranslate(x, y, z)
      self.materialize()
      gluCylinder(self.getQuadric(),
          self.base,
          self.top,  
          self.height,  
          self.slices,  
          self.stacks)
      glPopMatrix()

