#/******************************************************************************
# 
#  Copyright (c) 2018 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
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

# 2018/09/05 Updated.

#  ZImageView.py

# encodig: utf-8

import sys
import os
import traceback
import numpy as np
from PIL import Image

#---------------------------------------------------------------------

class ZPILImageCropper():

  def __init__(self, filename =None):
    self.image = None #Pillow image
    self.filename = filename
    if self.filename != None:
      #  Load an image from the filaname as Pillow image format.  
      self.image = Image.open(filename)
      

  def crop_maximum_square_region(self, cropped_filename):
    if self.image != None:
      # Crop max square region from the self.image, and save it as a cropped_file.
      w, h  = self.image.size
      ms    = min([w, h])
      self.cropped_image = self.image.crop(((w - ms) // 2, (h - ms) // 2,
                                       (w + ms) // 2, (h + ms) // 2))

      self.cropped_image.save(cropped_filename)

 
  def crop_largest_central_square_region(self):
    if self.image != None:
      # Crop max square region from the self.image, and save it as a cropped_file.
      w, h  = self.image.size
      ms    = min([w, h])
      self.cropped_image = self.image.crop(((w - ms) // 2, (h - ms) // 2,
                                       (w + ms) // 2, (h + ms) // 2))

      return self.cropped_image
      

 
