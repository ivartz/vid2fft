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
 
#  ZOpenGLMultiTexturedBox.py

# encodig: utf-8

import numpy as np
import math
import OpenGL

from SOL4Py.opengl.ZOpenGLTexture2D import *
from SOL4Py.opengl.ZTextureCoordTriangularBox import *
from SOL4Py.opengl.ZOpenGLImageInfo import *


class ZOpenGLMultiTexturedBox(ZOpenGLObject):

  FACES = 6
  

  def __init__(self, w, h, z):
    super().__init__()
    self.texture = []
    self.ttb     = None
    self.w = w
    self.h = h
    self.z = z

  def createTexture(self, size, filenames):
    self.ttb = None

    if size != self.FACES:
      raise ValueError("Invalid size parameter:" + str(size))
   
    if filenames == None:
      raise ValueError("Invalid filenames parameter")
      
    self.textures = []    

    for i in range(self.FACES):
      self.textures.append(ZOpenGLTexture2D())
    
    self.ttb = self.createBox(self.w, self.h, self.z)
    
    self.load(size, filenames)


  def createTextureFromImageInfo(self, size, imageInfos):  # ZOpenGLImageInfo
    self.ttb = None

    if size != self.FACES:
      raise ValueError("Invalid size parameter:" + str(size))
         
    self.textures = []    

    for i in range(self.FACES):
      self.textures.append(ZOpenGLTexture2D())
    
    self.ttb = self.createBox(self.w, self.h, self.z)

    self.setImageInfo(size, imageInfos)


  # Refine your own method in a sublcass derived from this class.  
  def createBox(self, w, h, z):
    return ZTextureCoordTriangularBox(w, h, z)
    
    
  def load(self, size, filenames):

    for i in range(self.FACES): 
      self.textures[i].bind()

      self.textures[i].pixelStore(GL_UNPACK_ALIGNMENT, 1)

      self.textures[i].parameter(GL_TEXTURE_MAG_FILTER, GL_LINEAR)
      self.textures[i].parameter(GL_TEXTURE_MIN_FILTER, GL_LINEAR)
      self.textures[i].env(GL_TEXTURE_ENV_MODE, GL_MODULATE)

      self.textures[i].generate(GL_S, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)
      self.textures[i].generate(GL_T, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)

      self.textures[i].parameter(GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
      self.textures[i].parameter(GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
      
      self.textures[i].imageFromFile(filenames[i]) # GL_TEXTURE_2D)
    
      self.textures[i].unbind()

  def setImageInfo(self, size, imageInfos):
    if (size != self.FACES) :
      raise ValueError("Invalid size parameter: " + str(size))
    
    if (imageInfos ==  None) :
      raise ValueError("Invalid imageInfos parameter")

    for i in range(self.FACES):
      self.textures[i].bind()

      self.textures[i].pixelStore(GL_UNPACK_ALIGNMENT, 1) ##4)

      self.textures[i].parameter(GL_TEXTURE_MAG_FILTER, GL_LINEAR)
      self.textures[i].parameter(GL_TEXTURE_MIN_FILTER, GL_LINEAR)
      self.textures[i].env(GL_TEXTURE_ENV_MODE, GL_MODULATE)

      self.textures[i].generate(GL_S, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)
      self.textures[i].generate(GL_T, GL_TEXTURE_GEN_MODE, GL_NORMAL_MAP)

      self.textures[i].parameter(GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
      self.textures[i].parameter(GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
     
      self.textures[i].imageFromImageInfo(imageInfos[i])
    
      self.textures[i].unbind()


  def draw(self):
  
    box = self.ttb.getBox()
      
    numFaces = self.ttb.getNumberOfFaces()
    numVerticesPerFace = self.ttb.getNumberOfVerticesPerFace()
      
    glEnable(GL_NORMALIZE)
    glEnable(GL_BLEND)
    
    glEnable(GL_TEXTURE_2D)
        
    for i in range(numFaces):
      self.textures[i].bind()
      glBegin(GL_TRIANGLES)

      for j in range(numVerticesPerFace):
        cv = box[i*numFaces + j]
        self.textures[i].coordVertex(cv[0], cv[1])
       
      glEnd()
      self.textures[i].unbind()
          
    glDisable(GL_TEXTURE_2D) 

    glFlush()

 