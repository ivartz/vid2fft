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
 
#  ZOpenGLTexture.py

# encodig: utf-8

import numpy as np
import math
import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLTexture(ZOpenGLObject):
  ## Constructor
  def __init__(self, target = GL_TEXTURE_2D):
    super().__init__()
    self.target = target

    glEnable(self.target)

    self.id = glGenTextures(1)
    print(self.id)

  def gettexture(self):
    return self.id


  def bind(self):
    glBindTexture(self.target, self.id)


  def unbind(self):
    glBindTexture(self.target, 0)


  def parameter(self, name, value):
    glTexParameterf(self.target, name, value)


  def getTarget(self):
    return self.target


  def getTexture(self):
    return self.id

  def env(self, name, value):
    glTexEnvf(GL_TEXTURE_ENV, name, value)
 

  def coord1F(self, s):
    glTexCoord1f(s)

 
  def coord2F(self, s, t):
    glTexCoord2f(s, t)


  def coordVertex(self, coord, vertex): #TextureCoord2Vertex3& cube)
    glTexCoord2fv(coord)
    glVertex3fv(vertex)


  
  def coord2F(self, s, t):
    glTexCoord2f(s, t)  


  def coord3F(self, s, t, r):
    glTexCoord3f(s, t, r)


  def coord4F(self, s, t, r, q):
    glTexCoord4f(s, t, r, q)


  def coordFV(self, size, v):
    if size ==1: 
      glTexCoord1fv(v)
    if size == 2:
      glTexCoord2fv(v)
    if size == 3:
      glTexCoord3fv(v)
    if size == 4:
      glTexCoord4fv(v)


  def generate(self, coord, name, param):
    glTexGenf(coord, name, param) 


  def pixelStore(self, name, param): 
    glPixelStorei(name, param)


  def env(self, mode=GL_TEXTURE_ENV_MODE, value=GL_MODULATE):
    glTexEnvf(GL_TEXTURE_ENV, mode, value)
