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

#  ZOpenGLFragmentShader.py

# encoding: utf-8

import sys
import os
import traceback

import traceback
import numpy as np
import math
#import OpenGL

from SOL4Py.opengl2.ZOpenGLShader import *


#ifdef GL_VERSION_2_0


class ZOpenGLFragmentShader(ZOpenGLShader):
  ## Constructor
  def __init__(self):
    super().__init__(GL_FRAGMENT_SHADER)


#endif

