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
#  ZScrolledDecisionTreeView.py

# encodig: utf-8

import sys
import os
import traceback
import time
from sklearn import tree
import pydotplus as pdp

from SOL4Py.ZMain      import *

from SOL4Py.ZImageView import *
from PyQt5.QtWidgets   import *
from PyQt5.QtGui       import *
from PyQt5.QtCore      import *

from SOL4Py.ZScrolledImageView import *

#---------------------------------------------------------------------

class ZScrolledDecisionTreeView(ZScrolledImageView):

  def __init__(self, parent, x, y, width, height, keepAspectRatio=True):
    super(ZScrolledDecisionTreeView, self).__init__(parent, x, y, width, height, keepAspectRatio)
   
   
  def set_tree(self, decision_tree, feature_names=None, target_names=None):
    ctime = int(time.time() * 1000)
    
    filename = str(ctime) + ".png"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fullpath = os.path.join(current_dir, filename)
    
    try:
      dot_data = tree.export_graphviz(decision_tree,
                                out_file=None,
                                filled=True, 
                                rounded=True, 
                                feature_names=feature_names, 
                                class_names=target_names, 
                                special_characters=True 
                                )
      self.graph = pdp.graph_from_dot_data(dot_data)

      self.graph.write_png(fullpath)
      self.image_view.load_image(fullpath)
      os.remove(fullpath)

    except:
      print(formatted_traceback())

      
                                
                                