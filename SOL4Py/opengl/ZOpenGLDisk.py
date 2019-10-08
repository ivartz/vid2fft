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
 
#  ZOpenGLDisk.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLShape import *


class ZOpenGLDisk(ZOpenGLShape):
  
  def __init__(self, quadric, materia, inner=0.5, outer=1.0, slices=32, stacks=32):
    super().__init__(quadric, materia)
    self.reshape(inner, outer, slices, stacks)


  def reshape(self, inner, outer, slices, stacks):
    self.inner  = inner  
    self.outer  = outer  
    self.slices = slices
    self.stacks = stacks 


  def draw(self):
    gluDisk(self.quadric.getQuadric(),  
         self.inner,  
         self.outer,  
         self.slices,  
         self.stacks); 

