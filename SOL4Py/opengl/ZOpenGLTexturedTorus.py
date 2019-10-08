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
 
#  ZOpenGLTexturedTorus.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl.ZOpenGLQuadric import *
from SOL4Py.opengl.ZOpenGLMateria import *
from SOL4Py.opengl.ZOpenGLTexture2D import *
import math


class ZOpenGLTexturedTorus(ZOpenGLTexture2D):

  def __init__(self, filename=None, materia=None, r = 0.1, c = 0.2,
                                             r_seg = 40, c_seg=20):

    super().__init__()
    self.materia = materia

    self.r = r
    self.c = c
    
    self.r_seg = r_seg
    self.c_seg = c_seg
    if filename != None:
      self.load(filename)


  def load(self, filename, flip=True):
    self.bind()

    self.pixelStore(GL_UNPACK_ALIGNMENT, 4)
    
    self.parameter(GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    self.parameter(GL_TEXTURE_MIN_FILTER, GL_NEAREST)
  
    self.parameter(GL_TEXTURE_WRAP_S, GL_REPEAT)
    self.parameter(GL_TEXTURE_WRAP_T, GL_REPEAT)
    self.env(GL_TEXTURE_ENV_MODE, GL_MODULATE)

   
    self.imageFromFile(filename, 0, 0, flip=False)

    self.unbind()


  # This is based on the following c code:
  # https://gist.githubusercontent.com/gyng/8939105/raw/254c247610dfdf6f3369035f59dc06f78c65a7c5/torus.cpp

  def draw(self):
    self.bind()
    glFrontFace(GL_CW)
    glEnable(GL_NORMALIZE)

    pi2 = 2.0 * math.pi

    for i in range(self.r_seg):
      glBegin(GL_QUAD_STRIP)
      for j in range(self.c_seg+1):
        for k in range(2):
          s = (i + k) % self.r_seg + 0.5
          t = j % (self.c_seg + 1)

          x = (self.c + self.r * math.cos(s * pi2 / self.r_seg)) * math.cos(t * pi2 / self.c_seg)
          y = (self.c + self.r * math.cos(s * pi2 / self.r_seg)) * math.sin(t * pi2 / self.c_seg)
          z = self.r * math.sin(s * pi2 / self.r_seg )

          u = (i + k) / self.r_seg
          v = t / self.c_seg

          glTexCoord2f(u, v)
          glNormal3f(2 * x, 2 * y, 2 * z)
          glVertex3f(2 * x, 2 * y, 2 * z)
    
      glEnd()
      
    glDisable(GL_NORMALIZE)

    self.unbind()
      
