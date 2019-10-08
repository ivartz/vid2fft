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
 
#  ZOpenGLImage.py

# encodig: utf-8

import numpy as np

from PIL import Image, ImageOps
 
class ZOpenGLImage:
  
  # ZOpenGLImage Constructor
  def __init__(self, filename, flip=True):
    image = Image.open(filename)
    if flip == True:
      image = ImageOps.flip(image)
      
    self.width, self.height = image.size
    try:
      image = image.convert("RGBA")
      self.bytes = image.tobytes("raw", "RGBA", 0, -1)
    except SystemError:
      self.bytes = image.tobytes("raw", "RGBX", 0, -1)
