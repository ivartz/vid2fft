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
 
#  ZOpenGLTexturedCube.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLTexture2D import *
from SOL4Py.opengl.ZTextureCoordTriangularCube import *


class ZOpenGLTexturedCube(ZOpenGLTexture2D):
  ## Constructor
  
  def  __init__(self, filename=None, materia = None, size=1.0):
    super().__init__()
    self.materia = materia
    self.ttc = ZTextureCoordTriangularCube(size)
    if filename != None:
      self.load(filename)


  def load(self, filename):
  
    self.bind()

    self.pixelStore(GL_UNPACK_ALIGNMENT, 4)
    
    self.parameter(GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    self.parameter(GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    self.env(GL_TEXTURE_ENV_MODE, GL_MODULATE)
  
    self.generate(GL_S, GL_TEXTURE_GEN_MODE, GL_REFLECTION_MAP)
    self.generate(GL_T, GL_TEXTURE_GEN_MODE, GL_REFLECTION_MAP)

    self.parameter(GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    self.parameter(GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

    self.imageFromFile(filename)
    self.unbind()


  # This is a very slow drawing method
  def draw(self):
     cube = self.ttc.getBox()
     n_elements = self.ttc.getNumberOfElements()
      
     self.bind()
     glEnable(GL_NORMALIZE)
     glBegin(GL_TRIANGLES)
        
     for i in range(n_elements):
        self.coordVertex(cube[i])
     glEnd()
        
     self.unbind()
     

  def coordVertex(self, cube):
    glTexCoord2fv(cube[0]) #.coord.s, cube.coord.t)
    glVertex3fv(cube[1])   #.vertex.x, cube.vertex.y, cube.vertex.z)
 

 