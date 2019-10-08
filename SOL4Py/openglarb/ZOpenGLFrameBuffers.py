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
 
#  ZOpenGLFrameBuffers.py

# encodig: utf-8
import numpy as np
import OpenGL

from SOL4Py.opengl.ZOpenGLObject import *
from OpenGL.GL.ARB.vertex_buffer_object import *
from OpenGL.GL.EXT.framebuffer_object import *

#ifdef GL_ARB_framebuffer_object

class ZOpenGLFrameBuffers(ZOpenGLObject):

 
  ## Constructor
  def __init__(self, size, target):
    super().__init__()
 
    self.size   = size
    self.target = target
    self.buffer = None
    
    if size <= 0:
      raise ValueError("Invalid size parameter. size" + str(size)) ;
      
    self.buffer = glGenFramebuffers(self.size);


  def unbind(self):
    glBindFramebuffer(self.target, 0);

  def delete(self):
    glDeleteFramebuffers(self.size, self.buffers);  
  
  def blit(self, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, 
                dstX1, dstY1, mask, filter):
    
    glBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, 
           dstX1, dstY1, mask, filter);
  
  def check(self):
    return glCheckFramebufferStatus(self.target);


  def attachRenderbuffer(self, attachment, renderbuffertarget, renderbuffer):
    glFramebufferRenderbuffer(self.target, attachment, renderbuffertarget, renderbuffer);


  def detachRenderbuffer(self,attachment, renderbuffertarget):
    attachRenderbuffer(self.target, attachment, renderbuffertarget, 0);


  def texture1D(self, attachment, textarget, texture, level):
    glFramebufferTexture1D(self.target, attachment, textarget, texture, level);


  def texture2D(self, attachment, textarget, texture, level):
    glFramebufferTexture2D(self.target, attachment, textarget, texture, level);


  def texture3D(self, attachment, textarget, texture, level, zoffset):
    glFramebufferTexture3D(self.target, attachment, textarget, texture,level, zoffset);


  def getAttachmentParameteriv(self, attachment, pname):
    return glGetFramebufferAttachmentParameteriv(self.target, attachment, pname)


  def isFramebuffer(self):
    return glIsFramebuffer(self.buffer);


  def get(self, n=0):
    if self.size == 1:
      return self.buffers
  
    if n > 0 and n < self.size:
      return self.buffers[n];
    else:
      raise ValueError("Invalid index " + str(n));


  def bind(self, n=0):
    if self.size == 1:
      glBindFramebuffer(self.target, self.buffer);
    elif n > 0 and n < self.size:
      glBindFramebuffer(self.target, self.buffer[n]);
    else:
      raise ValueError("Invalid index " + str(n)) ;


#endif
  
  