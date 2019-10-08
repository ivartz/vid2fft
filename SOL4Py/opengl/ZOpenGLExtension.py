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
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/
 
#  ZOpenGLExtension.py

# encodig: utf-8

import sys
import os
import math
import traceback

import numpy as np

import OpenGL
import OpenGL.GL as gl

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

 
class ZOpenGLExtension:

  # ZOpenGLObject Constructor
  def __init__(self):
    self.extensions = glGetString(GL_EXTENSIONS)
    self.extensions = self.extensions.split()
    
    
  def isSupported(self, name):
    name = name.encod("utf-8")
    rc = False
    for extension in self.extensions:
      if extension == name:
        self.SUPPORT_EXTENSION = True
        print("supported " + name)
        rc = True
        break
    return rc
    
  def get_extensions(self):
    extensions = []
    for name in self.extensions:
      extensions.append(str(name))
    return extensions
    
     
  def isGL_ARB_vertex_buffer_object(self):
    return self.isSuppored("GL_ARB_vertex_buffer_object")

