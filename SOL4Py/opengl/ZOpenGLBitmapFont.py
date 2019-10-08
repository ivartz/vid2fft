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
 
#  ZOpenGLBitmapFont.py

# encodig: utf-8

import sys

# 

from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLBitmapFont(ZOpenGLObject):
  ## Construcotr
  
  def __init__(self, font = GLUT_BITMAP_TIMES_ROMAN_24):
    if self.isBitmapFont(font):
      self.font = font
    else:
      raise ValueError("Invalid font name")

  
  def draw(self, x, y, z, text):
    if text == None:
      return

    self.text = text
  
    size = len(self.text)
    glPushMatrix()
    glRasterPos3f(x, y,z)
    for i in range(size):
      glutBitmapCharacter(self.font, ord(self.text[i]))
    glPopMatrix()


  def isBitmapFont(self, font):
    fonts = [
       GLUT_BITMAP_9_BY_15,
       GLUT_BITMAP_8_BY_13,
       GLUT_BITMAP_TIMES_ROMAN_10,
       GLUT_BITMAP_TIMES_ROMAN_24,
       GLUT_BITMAP_HELVETICA_10,
       GLUT_BITMAP_HELVETICA_12,
       GLUT_BITMAP_HELVETICA_18,
     ]
    rc = False
    for i in range(len(fonts)):
      if  font == fonts[i]:
        rc = True
        break
    return rc

