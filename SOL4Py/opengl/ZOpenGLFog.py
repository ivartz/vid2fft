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
 
#  ZOpenGLFog.py

# encodig: utf-8

import sys

# 

from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLFog(ZOpenGLObject):

  def __init__(self):
    super().__init__()


  def enable(self):
    glEnable(GL_FOG)


  def disable(self):
    glDisable(GL_FOG)

 
  #mode = GL_LINEARr, AGL_EXP, AGL_EXP2 
  def mode(self,  mode = GL_LINEAR):
    glFogi(GL_FOG_MODE, mode)


  def density(self,  value):
    glFogf(GL_FOG_DENSITY, value)


  #Specify start position for GL_LINEAR mode
  def start(self,  value):
    glFogf(GL_FOG_START, value)


  #Specify end position for GL_LINEAR mode
  def end(self,  value):
    glFogf(GL_FOG_END, value)


  #Specify color index
  def index(self,  value):
    glFogf(GL_FOG_INDEX, value)


  #Specify color index
  def color(self, value):
    glFogfv(GL_FOG_COLOR, value)


  def color(self,  r,  g,  b,  a):
    value = [r, g, b, a]
    glFogfv(GL_FOG_COLOR, value)


  #def color(self, value):
  #  glFogiv(GL_FOG_COLOR, value)
  



