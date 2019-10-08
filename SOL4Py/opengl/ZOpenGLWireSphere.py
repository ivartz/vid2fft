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
 
#  ZOpenGLWireSphere.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLGeometry import *
from SOL4Py.opengl.ZOpenGLMateria import *

class ZOpenGLWireSphere(ZOpenGLGeometry):

  ## Constructor
  def __init__(self, materia, radius, slices, stacks):
    super().__init__(materia)
    
    self.reshape(radius, slices, stacks)


  def reshape(self, radius, slices, stacks):
    self.radius = radius
    self.slices = slices
    self.stacks = stacks


  def draw(self):
    glPushMatrix();
    self.materialize();
    self.wireSphere(self.radius, self.slices, self.stacks);
    glPopMatrix();

