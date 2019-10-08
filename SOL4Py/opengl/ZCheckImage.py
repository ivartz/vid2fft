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
 
#  ZCheckImage.py

# encodig: utf-8

import math
import numpy as np

class ZCheckImage:
  WIDTH  = 8
  HEIGHT = 8

  ##
  # Constructor
  
  def __init__(self):
  
    # Create a texture from a RGBA checker board image of size WIDHT and HEIGHT 
    data= np.zeros(self.WIDTH * self.HEIGHT * 4, dtype=np.byte).reshape((self.WIDTH, self.HEIGHT, 4))

    for i in range(self. HEIGHT):
      for j in range(self.WIDTH):
        if (i + j) % 2 == 0: 
          c = 255  
          # white
          data[i][j][0] = np.byte(c)
          data[i][j][1] = np.byte(c)
          data[i][j][2] = np.byte(c)
        else:
          c= 255 
          # red
          data[i][j][0] = np.byte(c)   
          data[i][j][1] = 0 
          data[i][j][2] = 0 
 
        data[i][j][3] = 0 
        
    self.data = data
    

