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
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/
 
#  ZOpenGLShape.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl.ZOpenGLMateria import *
from SOL4Py.opengl.ZOpenGLQuadric import *


class ZOpenGLShape(ZOpenGLObject):
  
  #OpenGLShape(OpenGLQuadric quardic, ZOpenGLMateria materia)
  def __init__(self, quadric, materia=None):
    super().__init__()
    self.quadric = quadric
    self.materia = materia


  def getQuadric(self): 
    return self.quadric.getQuadric()  # GluQuadric

  def materialize(self, flags=ZOpenGLMateria.ALL_MATERIAS):
    self.materia.materialize(flags);

  # Define your own draw method in a subclass derived from this class.
  def draw(self):
    pass  


