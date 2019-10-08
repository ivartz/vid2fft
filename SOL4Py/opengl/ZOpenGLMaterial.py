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
 
#  ZOpenGLMaterial.py

# encodig: utf-8

from SOL4Py.ZColor4 import *
from SOL4Py.opengl.ZOpenGLObject import *

class ZOpenGLMaterial(ZOpenGLObject):

  def __init__(self, face):
    super().__init__()
    #The parameter face will take CL_FRONT, CL_BACK, CL_FRONT_AND_BACK 
    self.face = face


  def ambientv(self, values):
    glMaterialfv(self.face , GL_AMBIENT , values) 
  

  def ambient(self, r,  g,  b,  a):
    values = [r, g, b, a]
    glMaterialfv(self.face , GL_AMBIENT , values) 


  def diffusev(self, values):
    glMaterialfv(self.face , GL_DIFFUSE, values) 
  

  def diffuse(self, r,  g,  b,  a):
    values = [r, g, b, a]
    glMaterialfv(self.face , GL_DIFFUSE, values) 
  

  def specularv(self, values):
    glMaterialfv(self.face , GL_SPECULAR, values) 
  

  def specular(self, r,  g,  b,  a):
    values = [r, g, b, a]
    glMaterialfv(self.face , GL_SPECULAR, values) 


  def shininessv(self, values):
    glMaterialfv(self.face , GL_SHININESS, values) 


  def shininess(self, shine):
    values = [shine]
    glMaterialfv(self.face , GL_SHININESS, values) 


  def emissionv(self, values):
    glMaterialfv(self.face , GL_EMISSION, values) 
  

  def emission(self, r,  g,  b,  a):
    values = [r, g, b, a]
    glMaterialfv(self.face , GL_EMISSION, values) 


  def ambientAndDiffuse(self, values):
    glMaterialfv(self.face, GL_AMBIENT_AND_DIFFUSE, values) 


  def colorIndexes(self, values):
    glMaterialfv(self.face , GL_COLOR_INDEXES, values) 
  

  def colorIndexes(self, r,  g,  b):
    values = [r, g, b] 
    glMaterialfv(self.face, GL_COLOR_INDEXES, values) 
  

