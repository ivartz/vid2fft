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
 
#  ZOpenGLQuadric.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *


class ZOpenGLQuadric(ZOpenGLObject):

  def __init__(self):
    super().__init__()
    self.quadric = gluNewQuadric()


  def delete(self):
    gluDeleteQuadric(self.quadric)


  def getQuadric(self):
    return self.quadric


  def orientation(self, orientation): #GLenum 
    #orientation will take GLU_OUTSIDE, and GLU_INSIDE
    gluQuadricOrientation(self.quadric, orientation)


  def texture(self, texture): #GLboolean
    gluQuadricTexture(self.quadric, texture)


  def drawStyle(self, style):  #GLenum 
    #style will take GLU_FILL, GLU_LINE, GLU_SILHOUETTE, and GLU_POINT. 
    gluQuadricDrawStyle(self.quadric, style)


  def normals(self, normal):  #GLenum 
    #normal will take GLU_NONE, GLU_FLAT, and GLU_SMOOTH
    gluQuadricNormals(self.quadric, normal)

