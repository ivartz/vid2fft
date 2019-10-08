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
 
#  ZColoredCheckImage.py

# encodig: utf-8

import math
import numpy as np

class ZColoredCheckImage:
  WIDTH  = 64
  HEIGHT = 64

  ##
  # Constructor
  
  def __init__(self, r=True, g=True, b=True):
  
    # Create a texture from a RGBA black and white checker board image of size WIDHT and HEIGHT 
    data= np.zeros(self.WIDTH * self.HEIGHT * 4, dtype=np.byte).reshape((self.WIDTH, self.HEIGHT, 4))

    for i in range(self. HEIGHT):
      for j in range(self.WIDTH):
        c = (((i & 0x8) == 0) ^ ((j & 0x8) == 0)) * 255;
        if r == True:
          data[i][j][0] = np.byte(c)
        else:
          data[i][j][0] = np.byte(255)
        if g == True:
          data[i][j][1] = np.byte(c)
        else:
          data[i][j][1] = np.byte(255)
          
        if b == True:
          data[i][j][2] = np.byte(c)
        else:
          data[i][j][2] = np.byte(255)
          
        data[i][j][3] = np.byte(255)
      
    self.data = data
    

