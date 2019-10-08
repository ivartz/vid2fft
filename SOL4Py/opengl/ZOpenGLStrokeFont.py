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
 
#  ZOpenGLStrokeFont.py

# encodig: utf-8

import sys

# 

from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLStrokeFont(ZOpenGLObject):
  ## Constructor
  
  def __init__(self, font = GLUT_STROKE_ROMAN):
    if self.isStrokeFont(font):
      self.font = font
    else:
      raise ValueError("Invalid font")
      

  def draw(self, x, y, z, text, scale=0.2):
    if text == None:
      return
    else:
      self.text = text
            
    size = len(self.text)
    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(scale, -1.0*scale, scale)
    for i in range(size):
      glutStrokeCharacter(self.font, ord(self.text[i]))
    glPopMatrix()
  
  
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


