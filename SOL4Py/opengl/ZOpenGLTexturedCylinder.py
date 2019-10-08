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
 
#  ZOpenGLTexturedCylinder.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl.ZOpenGLQuadric import *
from SOL4Py.opengl.ZOpenGLMateria import *
from SOL4Py.opengl.ZOpenGLTexture2D import *
from SOL4Py.opengl.ZOpenGLCylinder import *
import math


class ZOpenGLTexturedCylinder(ZOpenGLTexture2D):

  def __init__(self, filename, materia=None, base=2.0,  top=1.0, height=2.0, slices=40, stacks=40):
    super().__init__()
    self.materia = materia
    self.quadric = ZOpenGLQuadric();
    if self.materia == None:
      self.materia = ZOpenGLMateria()
      
    texture= self.gettexture()
    
    self.quadric.texture(texture);
      
    self.cylinder = ZOpenGLCylinder(self.quadric, self.materia)
    self.cylinder.reshape(base, top, height, slices, stacks)

    self.load(filename);
    self.drawStyle(GLU_FILL);
 

  def drawStyle(self, style):
    #style will take GLU_FILL, GLU_LINE, GLU_SILHOUETTE, and GLU_POINT. 
    self.quadric.drawStyle(style);    
  
  def orientation(self, orientation):
    #orientation will take GLU_OUTSIDE, and GLU_INSIDE
    self.quadric.orientation(orientation);

 
  def normals(self, normal):
    #normal will take GLU_NONE, GLU_FLAT, and GLU_SMOOTH
    self.quadric.normals(normal);
 

  def load(self, filename):
    self.bind();

    self.pixelStore(GL_UNPACK_ALIGNMENT, 4);
    
    self.parameter(GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    self.parameter(GL_TEXTURE_MIN_FILTER, GL_NEAREST);

    self.parameter(GL_TEXTURE_WRAP_S, GL_REPEAT);
    self.parameter(GL_TEXTURE_WRAP_T, GL_REPEAT);
    self.env(GL_TEXTURE_ENV_MODE, GL_MODULATE)

    self.imageFromFile(filename);
    self.unbind();
 


  def draw(self):  
    self.bind();
    self.cylinder.draw();
    self.unbind()
