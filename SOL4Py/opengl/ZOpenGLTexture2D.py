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
 
#  ZOpenGLTexture2D.py

# encodig: utf-8

import numpy as np
import math
import OpenGL

from SOL4Py.opengl.ZOpenGLTexture import *
from SOL4Py.opengl.ZOpenGLImage import *
from SOL4Py.opengl.ZOpenGLImageInfo import *


class ZOpenGLTexture2D(ZOpenGLTexture):

  ## Constructor
  def __init__(self):
    super().__init__(GL_TEXTURE_2D)


  def image(self, level, components,
       width, height, border,
       format, type, pixels):
       
    glTexImage2D(self.getTarget(),
        level, components,
        width, height, border,
        format, type, pixels) 
  
  # Create a texturedImage from an imageInfo (OpenGLImageInfo)
  def imageFromImageInfo(self, imageInfo):
    glTexImage2D(self.getTarget(),
        0, imageInfo.format,
        imageInfo.width, imageInfo.height, 0,
        imageInfo.format, imageInfo.type, imageInfo.imageData) 
    

  def imageFromFile(self, filename, level=0,  border=0, flip=True):
    if filename == None:
      raise ValueError("Invalid argument")

    self.image = ZOpenGLImage(filename, flip)
    w = self.image.width
    h = self.image.height
    glTexImage2D(self.getTarget(), 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.image.bytes)


  def subImage(self, level,  
                xoffset,  
                yoffset,  
                width,  
                height,  
                format,  
                type,  
                data):
    glTexSubImage2D(self.getTarget(), level, xoffset, yoffset, width, height, format, type, data) 


  def subImageFromFile(self, filename, level, xoffset, yoffset):
    if filename == None:
      raise ValueError("Invalid argument")
    
    self.image = ZOpenGLImage(filename)
    w = self.image.width
    h = self.image.height
      
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.image.bytes)
    glTexSubImage2D(self.getTarget(), level, xoffset, yoffset, w, h,  
        GL_RGBA, GL_UNSIGNED_BYTE, self.image.bytes)


  def mipmap(self, internalFormat, width, height, format, type, data): 
    gluBuild2DMipmaps(self.getTarget(), 
        internalFormat,  
        width,  
        height,  
        format,  
        type,  
        data)


  def mipmapFromFile(self, filename):
    if filename == None:
      raise ValueError("Invalid argument")

    self.image = ZOpenGLImage(filename)
    w = self.image.width
    h = self.image.height

    self.mipmap(GL_RGBA, w, h, GL_RGBA, GL_UNSIGNED_BYTE, self.image.bytes)
 

