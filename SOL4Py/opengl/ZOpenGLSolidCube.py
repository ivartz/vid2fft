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
 
#  ZOpenGLSolidCube.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLGeometry import *


class ZOpenGLSolidCube(ZOpenGLGeometry):

  def __init__(self, materia, size):
    super().__init__(materia)
    self.size = size
  
  def draw(self, x=0.0, y=0.0, z =0.0):
    glPushMatrix()
    glTranslate(x, y, z)
    self.materialize()
    self.solidCube(self.size)
    glPopMatrix()

