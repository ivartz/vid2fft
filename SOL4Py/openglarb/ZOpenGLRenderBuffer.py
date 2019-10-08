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
 
#  ZOpenGLRenderBuffer.py

# encodig: utf-8
import numpy as np
import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.openglarb.ZOpenGLRenderBuffers import *


#ifdef GL_ARB_framebuffer_object


class ZOpenGLRenderBuffer(ZOpenGLRenderBuffers):

  def __init__(self):
    super().__init__(1, GL_RENDERBUFFER)
  
  
  def bind(self):
    if self.size == 1:
      glBindFramebuffer(self.target, self.buffer);


#endif
  
  