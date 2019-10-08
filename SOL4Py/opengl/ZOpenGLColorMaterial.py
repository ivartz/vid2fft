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
 
#  ZOpenGLColorMaterial.py


# encodig: utf-8

import numpy as np
import math

from ctypes import *

from SOL4Py.opengl.ZOpenGLIndexedVertices import *


class ZOpenGLColorMaterial(ZOpenGLObject):

  ## Constructor
  def __init__(self, face, mode):
    
    self.face = face
    self.mode = mode

    #The parameter face will take CL_FRONT, CL_BACK, CL_FRONT_AND_BACK    
    #The parameter mode will take GL_EMISSION, GL_AMBIENT, GL_DIFFUSE, 
    #GL_SPECULAR, and GL_AMBIENT_AND_DIFFUSE. 
    # The initial value is GL_AMBIENT_AND_DIFFUSE. 

    glColorMaterial(face, mode);


  def enable(self):
    glEnable(GL_COLOR_MATERIAL);


  def disable(self):
    glDisable(GL_COLOR_MATERIAL);
  
