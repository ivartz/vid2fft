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
 
#  ZOpenGLIndexBufferARB.py

# encodig: utf-8


from SOL4Py.openglarb.ZOpenGLBufferARB import *


#ifdef GL_ARB_vertex_buffer_object


class ZOpenGLIndexBufferARB(ZOpenGLBufferARB):
  ## Constructor
  def __init__(self):
    super().__init__(GL_ELEMENT_ARRAY_BUFFER_ARB)

#endif

