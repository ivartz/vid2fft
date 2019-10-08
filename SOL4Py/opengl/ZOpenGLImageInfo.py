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
 
#  ZOpenGLImageInfo.py

# encodig: utf-8

import numpy as np

from SOL4Py.opengl.ZOpenGLObject import *
 
class ZOpenGLImageInfo(ZOpenGLObject):

  def __init__(self, xinternal = GL_RGBA, 
                     xformat   = GL_BGRA, 
                     xtype     = GL_UNSIGNED_BYTE):
                     
    self.depth       = 0
    #self.xformat    = 0
    self.internalFormat = xinternal
    self.width          = 0
    self.height         = 0
    self.format         = xformat
    self.type           = xtype
    self.widthStep      = 0
    self.imageSize      = 0
    self.imageData      = None # SmartPtrs<uint32_t>  imageData;

