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
 
#  ZOpenGLMultiTextureCube.py

# encodig: utf-8

import numpy as np
import math
import OpenGL

from SOL4Py.opengl.ZOpenGLMultiTexturedBox import *
from SOL4Py.opengl.ZTextureCoordTriangularCube import *


class ZOpenGLMultiTexturedCube(ZOpenGLMultiTexturedBox):
  ## Constructor
  def __init__(self, size =1.0):
    super().__init__(size, size, size)


  def createBox(self, w, h, z):
    return ZTextureCoordTriangularCube(w) 

