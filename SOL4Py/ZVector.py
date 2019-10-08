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
 
#  ZVector.py

# encodig: utf-8

class ZVector:

  def __init__(self, size):
    self.size = size
    if size < 1:
      raise ValueError("VectorF: invalid size")
     
    self.v = [0.0 for i in range(size)]


  def set(self,i, value):  
    if i<0 or i >=self.size:
      raise ValueError("VectorF: invalid index")
    self.v[i] = value


  def get(self,i):  
    if i<0 or i >=self.size:
      raise ValueError("VectorF: invalid index")
    return self.v[i]


  def put(self, list):
    if len(list) != self.size:
      raise ValueError("VectorF: invalid size")
    self.v = list


  def vector(self):
     return self.v


  def to_array(self):
    return np.array(self.vector, "float32")

