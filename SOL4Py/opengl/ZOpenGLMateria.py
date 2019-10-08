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
 
#  ZOpenGLMateria.py

# encodig: utf-8

from SOL4Py.ZColor4 import *
from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLMateria(ZOpenGLObject):
  # class variables (static const int) 
    
  AMBIENT   =0x00001
  DIFFUSE   =0x00010
  SPECULAR  =0x00100
  EMISSION  =0x01000
  SHININESS =0x10000
  
  ALL_MATERIAS = (AMBIENT|DIFFUSE|SPECULAR|EMISSION|SHININESS)


  #The face parameter face will take GL_FRONT, GL_BACK, GL_FRONT AND GL_BACK
  def __init__(self, face=0, ambient=[0.0, 0.0, 0.0, 0.0],  diffuse=[0.0, 0.0, 0.0, 0.0],  
           specular=[0.0, 0.0, 0.0, 0.0], emission=[0.0, 0.0, 0.0, 0.0], shininess=0.0):
    super().__init__()
    
    self.face = face
    self.enabled = False
    
    self.initialize()
    self.update(face, ambient,  diffuse,  specular, emission, shininess)

  def  initialize(self):
    self.ambient  = [0.0, 0.0, 0.0, 0.0]
    self.diffuse  = [0.0, 0.0, 0.0, 0.0]
    self.specular = [0.0, 0.0, 0.0, 0.0]
    self.emission = [0.0, 0.0, 0.0, 0.0]

    self.shininess = 0.0


  def update(self, face, ambient,  diffuse,  specular, emission, shininess):
    self.face = face
    self.enabled = True
 
    self.ambient   = ambient
    self.diffuse   = diffuse
    self.specular  = specular
    self.emission  = emission
    self.shininess = shininess


  def copy(self, mat):
    self.initialize()
    self.face      = mat.face
    self.ambient   = mat.ambient
    self.diffuse   = mat.diffuse
    self.specular  = mat.specular
    self.emission  = mat.emission
    self.shininess = mat.shininess
    self.enabled   = mat.enabled


  def enable(self):
    self.enabled = True


  def disable(self):
    self.enabled = False


  def face(self, face):
    self.face = face


  def face():
    return self.face


  def ambient(self, color):
    self.ambient = color


  def ambient(self, value):
    if len(value) == 4:
      self.ambient = value


  def diffuse(self, value):
    if len(value) == 4:
      self.diffuse = value


  def specular(self, value):
    if len(value) == 4:
      self.specular = value



  def shininess(self, shine):
    self.shininess = shine


  def emission(self, color):
    self.emission = color



  def materialize(self, flags=ALL_MATERIAS):
    if self.enabled == True:
      if flags &  self.AMBIENT: 
        if self.ambient != None:
          glMaterialfv(self.face , GL_AMBIENT , self.ambient)# value) 
      
      if flags & self.DIFFUSE:
        if self.diffuse != None:
          glMaterialfv(self.face , GL_DIFFUSE, self.diffuse) 
      
      if flags & self.SPECULAR: 
        if self.specular != None:
          glMaterialfv(self.face , GL_SPECULAR, self.specular) 
      
      if flags & self.EMISSION: 
        if self.emission != None:
          glMaterialfv(self.face , GL_EMISSION, self.emission)    
      
      if flags & self.SHININESS:
        glMaterialfv(self.face , GL_SHININESS,[self.shininess]) 
      
