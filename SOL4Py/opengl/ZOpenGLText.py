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
 
#  ZOpenGLText.py

# encodig: utf-8

import sys

# 

from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLText(ZOpenGLObject):

  def __init__(self, text):
    self.text = text


  def draw(self, x, y, z, scale=1.0, font = GLUT_STROKE_ROMAN):
    if self.text == None:
      return
  
    size = len(self.text)
    if self.isStrokeFont(font):
      glPushMatrix()
      glTranslatef(x, y, z)
      glScalef(scale, -1.0*scale, scale)
      for i in range(size):
        glutStrokeCharacter(font, ord(self.text[i]))
      glPopMatrix()
       
    elif self.isBitmapFont(font):
      glPushMatrix()
      glRasterPos3f(x, y,z)
      for i in range(size):
        glutBitmapCharacter(font, ord(self.text[i]))
      glPopMatrix()
    else:
      raise ValueError("Invalid font")
  
  
  def isStrokeFont(self, font):
    fonts = [
       GLUT_STROKE_ROMAN,
       GLUT_STROKE_MONO_ROMAN,
     ]
    rc = False
    for i in range(len(fonts)):
      if  font == fonts[i]:
        rc = True
        break
    return rc


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

