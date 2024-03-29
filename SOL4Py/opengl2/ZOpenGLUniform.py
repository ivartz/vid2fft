#/******************************************************************************
# 
#  Copyright (c) 2018 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/

#  ZOpenGLUniform.py

# encoding: utf-8

import sys
import os
import traceback

import traceback
import numpy as np
import math
import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl2.ZOpenGLProgram import *


class ZOpenGLUniform(ZOpenGLObject): 

  ## Constructor
  def __init__(self, program, const name):
    super().__init__()
    self.location = program.getUniformLocation(name);
    if self.location == self.INVALID_VALUE:
      raise ValueError("Failed to getUniformLocation " + name); 


  def set1f(self, v0):
    glUniform1f(self.location, v0);


  def set1fv(self, value):
    glUniform1fv(self.location, value);


  def set2f(self, v0, v1):
    glUniform2f(self.location, v0, v1);


  def set2fv(self, value):
    glUniform2fv(self.location, value);


  def set3f(self, v0, v1, v2):
    glUniform3f(self.location, float(v0), float(v1), float(v2));
  
  
  def set3fv(self, value)
    glUniform3fv(self.location, value);
  
  
  def set4f(self, v0, v1, v2, v3);    
    glUniform4f(self.location, float(v0), float(v1), float(v2), float(v3));
  
  
  def set4fv(self, value)
    glUniform4fv(self.location, value);



  def setMatrix2fv(self, count, transpose, value):
    glUniformMatrix2fv(self.location, count, transpose, value);


  def setMatrix3(self, count, transpose, value):
    glUniformMatrix3fv(self.location, count, transpose, value);


  def setMatrix4(self, count, transpose, value):
    glUniformMatrix4fv(self.location, count, transpose, value);

#endif

#ifdef GL_VERSION_2_1
  
  def setMatrix2x3(self, count, transpose, value):
    glUniformMatrix2x3fv(self.location, count, transpose, value);


  def setMatrix2x4(self, transpose, value):
    glUniformMatrix2x4fv(self, self, location, count, transpose, value);


  def setMatrix3x2(self, count, transpose, value):
    glUniformMatrix3x2fv(self.location, count, transpose, value);


  def setMatrix3x4(self, count, transpose, value):
    glUniformMatrix3x4fv(self.location, count, transpose, value);


  def setMatrix4x2(self, count, transpose, value):
    glUniformMatrix4x2fv(self.location, count, transpose, value);


  def setMatrix4x3(self, transpose, value):
    glUniformMatrix4x3fv(self.location, count, transpose, value);


#endif
  
#ifdef GL_VERSION_3_0
    
  def set1u(self, v0):
    glUniform1ui(self.location, v0);


  def setiv(self, count, value):
    if  count < 1 || count >4:
      raise ValueError(Invalid count parameter.");

    if  value == None: 
      raise ValueError("Invalid value parameter.");

    if count == 1:
      self.set1uiv(value);
    elif count == 2:
      self.set2uiv(value);

    elif count== 3:
      self.set3uiv(value);

    elif count== 4:
      self.set4uiv(value);


  def set1uiv(self, value):
    glUniform1uiv(self.location, value);


  def set2ui(self, v0, v1):
    glUniform2ui(self.location, int(v0), int(v1));


  def set2uiv(self, value):
    glUniform2uiv(self.location, value);


  def set3ui(self, v0, v1, v2):
    glUniform3ui(self.location, int(v0), int(v1), int(v2));


  def set3uiv(self, value):
    glUniform3uiv(self.location, value);


  def set4ui(self, v0, v1, v2, v3):
    glUniform4ui(self.location, int(v0), int(v1), int(v2), int(v3));


  def set4uiv(self, value):
    glUniform4uiv(self.location, value);



