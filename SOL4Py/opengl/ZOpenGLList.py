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
 
#  ZOpenGLList.py

# encodig: utf-8

from SOL4Py.opengl.ZOpenGLObject import *
#from SOL4Py.opengl.ZOpenGLMateria import *


class ZOpenGLList(ZOpenGLObject):

  def __init__(self, list=1, mode=GL_COMPILE ):
    super().__init__()
 
    if list <= 0:
      raise ValueError("Invalid list id:%d", list)
 
    if glIsList(list) == GL_TRUE:
      raise ValueError("Already used " + str(list))
 
    if mode == GL_COMPILE or mode == GL_COMPILE_AND_EXECUTE:
      glNewList(list, mode)
    else:
      raise ValueError("Invalid mode " + str(mode)) 

    self.list = list
    self.mode = mode

  def call(self):
    #if (mode == 0) {
      glCallList(list)
    #

