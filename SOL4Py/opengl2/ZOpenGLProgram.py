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

#  ZOpenGLProgram.py

# encoding: utf-8

import sys
import os
import traceback

import numpy as np
import math

from SOL4Py.opengl.ZOpenGLObject import *

  
class ZOpenGLProgram(ZOpenGLObject): 

#ifdef GL_VERSION_2_0

  ## Constructor
  def __init__(self):
    super().__init__()
    self.program = self.create()
    if self. program == 0: 
      raise ValueError("Failed to glCreateProgram.")

  
  def attachShader(self, shader):
    glAttachShader(self.program, shader.shader)
  
  
  def bindAttributeLocation(self, index, name):
    glBindAttribLocation(self.program, index, name)


  def create(self):
    return glCreateProgram()


  def delete(self):
    glDeleteProgram(self.program)


  def detachShader(self, shader):
    glDetachShader(self.program, shader.shader)


  def getActiveAttribute(self, index):
    # length, size, type, name will be returned.
    return glGetActiveAttrib(self.program, index)
    
  
  def getAttachedShaders(self, maxCount):
    # count, shaders will be returned
    return glGetAttachedShaders(self.program, maxCount)


  def getAttributeLocation(self, name):
    return glGetAttribLocation(self.program, name)


  def getProgramInfoLog(self):
    # infoLog will be returned.
    return glGetProgramInfoLog(self.program)


  def getProgram(self):
    return self.program


  def getProgramiv(self, pname):
    return glGetProgramiv(self.program, pname)


  def getActiveAttributes(self):
    return self.getProgramiv( GL_ACTIVE_ATTRIBUTES)


  def getActiveAttributeMaxLength(self):
    return self.getProgramiv(GL_ACTIVE_ATTRIBUTE_MAX_LENGTH)
  

  def getActiveUniforms(self):
    return self.getProgramiv(ACTIVE_UNIFORMS)
  

  def getActiveUniformMaxLength(self):
    return self.getProgramiv(GL_ACTIVE_UNIFORM_MAX_LENGTH)
  

  def getAttachedShaders(self):
    return self.getProgramiv(GL_ATTACHED_SHADERS)


  def getDeleteStatus(self):
    return self.getProgramiv(GL_DELETE_STATUS)


  def getLinkStatus(self):
    return self.getProgramiv(GL_LINK_STATUS)


  def getValidateStatus(self):
    return self.getProgramiv(GL_VALIDATE_STATUS)


  def getUniformLocation(self):
    # This will return name of location.
    return glGetUniformLocation(self.program)
  
  
  def getUniform(self, location):
    # This will return params list
    return glGetUniformfv(self.program, location)
  


  def isProgram(self):
    return glIsProgram(self.program)


  def link(self):
    glLinkProgram(self.program)
    
    linked = self.getProgramiv(GL_LINK_STATUS)
    if linked == GL_FALSE: 
      raise ValueError(self, "Failed to link.")


  def use(self):
    glUseProgram(self.program)


  def unuse(self):
    glUseProgram(0)


  def validate(self):
    glValidateProgram(self.program)


#ifdef GL_VERSION_3_0
    
  def getUniform(self, ocation):
    # This will return params
    return glGetUniformuiv(self.program, location)
  
#endif

  



