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
 
#  ZOpenGLView.py

# encodig: utf-8

import sys
import numpy as np

from PIL import Image, ImageOps

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtOpenGL     import *

import OpenGL

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# 
from SOL4Py.opengl.ZOpenGLObject import *
from SOL4Py.opengl.ZOpenGLBitmap import *


##--------------------------------------------
class ZOpenGLView(QOpenGLWidget):

  def __init__(self, parent=None):
    self.parent = parent
    super(QOpenGLWidget, self).__init__(parent)

  # Please define your own method in a subclass derived from this class.
  def minimumSizeHint(self):
    return QSize(50, 50)

  # Please define your own method in a subclass derived from this class.
  def sizeHint(self):
    return QSize(400, 400)

  # Please define your own method in a subclass derived from this class.
  def initializeGL(self):
    pass

  # Please define your own method in a subclass derived from this class.
  def paintGL(self):
    pass
      
  # Please define your own method in a subclass derived from this class.
  def resizeGL(self, width, height):
    side = min(width, height)
    if side < 0: 
      return
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(20.0, width / height, 0.5, 100.0)

    glMatrixMode(GL_MODELVIEW)


  def save(self, filename):
    x      = self.x()
    y      = self.y()
    width  = self.width()
    height = self.height()
    u_filename = filename.upper()
   
    if u_filename.endswith(".JPG"):
      bitmap = ZOpenGLBitmap(x, y, width, height, 24, GL_RGB)
      pixels = bitmap.readPixels(GL_FRONT)
      image  = Image.frombytes("RGB", (width, height), pixels)

    elif u_filename.endswith(".PNG"):     
      bitmap = ZOpenGLBitmap(x, y, width, height, 24, GL_RGBA)
      pixels = bitmap.readPixels(GL_FRONT)
      image = Image.frombytes("RGBA", (width, height), pixels)
    else:
      bitmap = ZOpenGLBitmap(x, y, width, height, 24, GL_RGB)
      pixels = bitmap.readPixels(GL_FRONT)
      image  = Image.frombytes("RGB", (width, height), pixels)
       
    image = ImageOps.flip(image)
    image.save(filename)

 