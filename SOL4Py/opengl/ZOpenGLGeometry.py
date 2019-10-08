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
 
#  ZOpenGLGeometry.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl.ZOpenGLMateria import *


class ZOpenGLGeometry(ZOpenGLObject):

  def __init__(self, materia): #OpenGLMateria& materia)
    self.materia = materia

  def draw(x, y, z):
    pass
  
  def  wireCube(self, size):
    glutWireCube(size)
  

  def  solidCube(self, size):
    glutSolidCube(size)
  

  def  wireSphere(self, radius, slices, stacks):
    glutWireSphere(radius, slices, stacks)
  

  def  solidSphere(self, radius, slices, stacks):
    glutSolidSphere(radius, slices, stacks)
  

  def  wireCone(self, base, height, slices, stacks):
    glutWireCone(base, height, slices, stacks)
  

  def  solidCone(self, base, height, slices, stacks):
    glutSolidCone(base, height, slices, stacks)
  

  def  wireTorus(self, innerRadius, outerRadius, sides, rings):
    glutWireTorus(innerRadius, outerRadius, sides, rings)
  

  def  solidTorus(self, innerRadius, outerRadius, sides,  rings):
    glutSolidTorus(innerRadius, outerRadius, sides, rings)
  

  def  wireTeapot(self, value):
    glutWireTeapot(value)

  def  solidTeapot(self, value):
    glutSolidTeapot(value)
  

  def materialize(self, flags=ZOpenGLMateria.ALL_MATERIAS):
    if self.materia != None:
      self.materia.materialize(flags)
  
  
  def ambient(self,color):
    if self.materai != None:
      self.materia.ambient(color)
  

  def ambient(self, value):
    if self.materai != None:
      self.materia.ambient(value)
  

  def ambient(self, r, g, b, a):
    if self.materai != None:
      self.materia.ambient(r, g, b, a)


  def diffuse(self, color):
    if self.materai != None:
      self.materia.diffuse(color)


  def diffuse(self, value):
    if self.materai != None:
      self.materia.diffuse(value)
  

  def diffuse(self,  r,  g,  b,  a):
    if self.materai != None:
      self.materia.diffuse(r, g, b, a)
  

  def specular(self, color):
    if self.materai != None:
      self.materia.specular(color)
  

  def specular(self, value):
    if self.materai != None:
      self.materia.specular(value)
  

  def specular(self, r,  g,  b,  a):
    if self.materai != None:
      self.materia.specular(r, g, b, a)
  

  def shininess(self, shine):
    if self.materai != None:
      self.shininess(shine)
  

  def emission(self, color):
    if self.materai != None:
      self.materia.emission(color)
  

  def emission(self, value):
    if self.materai != None:
      self.materia.emission(value, size)
  

  def emission(self, r,  g,  b,  a):
    if self.materai != None:
      self.materia.emission(r, g, b, a)
  
  
  def draw(self, x, y, z):
    pass
    
