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
 
#  ZOpenGLLight.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl.ZOpenGLMateria import *


class ZOpenGLLight(ZOpenGLObject):

  def __init__(self, light=GL_LIGHT0):
    super().__init__()
    self.light = light
    #The light parameter will take GL_LIGHT0 to GL_LIGHT7
    glEnable(GL_LIGHTING)
    glEnable(self.light)
 
  def enable(self):
    glEnable(self.light)


  def ambientv(self, values):
    glLightfv(self.light, GL_AMBIENT, values)


  def ambient(self, r,  g,  b,  a):
    values = [r, g, b, a]
    glLightfv(self.light, GL_AMBIENT, values)


  def specularv(self, values):
    glLightfv(self.light,GL_SPECULAR, values)


  def specular(self, r,  g,  b,  a):
    values = [r, g, b, a]
    glLightfv(self.light,GL_SPECULAR, values)


  def diffusev(self, values):
    glLightfv(self.light, GL_DIFFUSE, values)


  def diffuse(self, r,  g,  b,  a):
    values = [r, g, b, a]
    glLightfv(self.light, GL_DIFFUSE, values)


  def positionv(self, values):
    glLightfv(self.light,GL_POSITION, values)


  def position(self, x,  y,  z,  w):
    values = [x, y, z, w]
    glLightfv(self.light,GL_POSITION, values)


  def spotDirection(self, values):
    glLightfv(self.light , GL_SPOT_DIRECTION , values) 


  def spotDirection(self, x,  y,  z):
    values = [x, y, z]
    glLightfv(self.light , GL_SPOT_DIRECTION , values) 


  def spotExponent(self, values):
    glLightfv(self.light , GL_SPOT_EXPONENT , values) 


  def spotExponent(self, v):
    values = [v]
    glLightfv(self.light , GL_SPOT_EXPONENT , values) 


  def spotCutoff(self, value):
    glLightfv(self.light , GL_SPOT_CUTOFF, value) 


  def spotCutoff(self, v):
    value = [v]
    glLightfv(self.light , GL_SPOT_CUTOFF, value) 


  def constantAttenuation(self, value):
    glLightfv(self.light , GL_CONSTANT_ATTENUATION, value) 


  def constantAttenuation(self, v):
    glLightfv(self.light , GL_CONSTANT_ATTENUATION, value) 


  def linearAttenuation(self, value):
    glLightfv(self.light , GL_LINEAR_ATTENUATION, value) 


  def linearAttenuation(self, v):
    value = [v]
    glLightfv(self.light , GL_LINEAR_ATTENUATION, value) 


  def quadraticAttenuation(self, value):
    glLightfv(self.light , GL_QUADRATIC_ATTENUATION, value) 


  def quadraticAttenuation(self, v):
    value = [v]
    glLightfv(self.light , GL_QUADRATIC_ATTENUATION, value) 

