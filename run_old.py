import sys
import os
import traceback

from SOL4Py.ZApplication         import *
from SOL4Py.ZLabeledComboBox     import *
from SOL4Py.ZLabeledSlider       import *
from SOL4Py.ZApplicationView     import *
from SOL4Py.opencv.ZOpenCVImageView     import ZOpenCVImageView
from SOL4Py.opencv.ZOpenCVVideoCapture  import ZOpenCVVideoCapture
import multiprocessing as mp
from time import sleep

def cam_process(message_queue, raw_video_queue, device=0):
  video_capture = ZOpenCVVideoCapture()
  video_capture.open(device)
  while True:
    try:
      """
      if not message_queue.empty():
        if message_queue.get() == "exit":
          print("fskdnhbfkjsdbhfhbk")
          #video_capture.close()
          #message_queue.close()
          #raw_video_queue.close()
          break
      """
      if video_capture.is_opened():
        frame = video_capture.read()
        raw_video_queue.put(frame)
        #raw_video_queue.put_nowait(frame) # non-blocking
    except KeyboardInterrupt:
        print("ignore CTRL-C from worker")
        print("to terminate child process correctly")
  print("Here")
  #video_capture.close()
  #message_queue.close()
  #raw_video_queue.close()

def start_cam_process(message_queue, raw_video_queue, device=0):
  p = mp.Process(target=cam_process, \
                             args=(message_queue, raw_video_queue, device))
  p.start()
  return p


class MainView(ZApplicationView):
  
  class SourceImageView(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)

    def load(self, filename):
      self.load_opencv_image(filename)
      self.update()
      
  """
  class SourceImageView_1(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)
      
  class SourceImageView_2(ZOpenCVImageView):
    def __init__(self, parent):
      ZOpenCVImageView.__init__(self, parent)
  """
  
  # Constructor
  def __init__(self, title, x, y, width, height, device=0):
    super(MainView, self).__init__(title, x, y, width, height)
    
    self.raw_video_queue = mp.Queue()
    self.message_queue = mp.Queue()
    
    """
    while queue_from_cam.empty():
      pass

    print 'getting image'
    from_queue = queue_from_cam.get()
    print 'saving image'
    cv2.imwrite('temp.png', from_queue)
    print 'image saved'    
    """
    
    #self.video_capture = ZOpenCVVideoCapture()
    #self.video_capture.open(device)
    
    self.image_view  = ZOpenCVImageView(self)
    
    #self.image_view  = self.SourceImageView_1(self)
    
    #self.image_view  = self.SourceImageView(self)
    
    #filename = "images/flower.png"
    #self.image_view_2 = self.SourceImageView(self)
    #self.image_view_2 = self.SourceImageView_2(self)
    self.image_view_2  = ZOpenCVImageView(self)
    #self.load_file(filename)
    
    filename = "images/flower.png"
    self.image_view_3 = self.SourceImageView(self)
    self.load_file(filename)
    
    self.add(self.image_view)
    self.add(self.image_view_2)
    self.add(self.image_view_3)

    title = str(device) + " - " + name
    self.setWindowTitle(title)
    
    self.show()
  
  # Read a frame from a video buffer of the video capture, and set it the image view to draw it on the imag view     
  def render(self):
    
    if not self.raw_video_queue.empty():
      #frame = self.raw_video_queue.get_nowait()
      frame = self.raw_video_queue.get()
      """
      if self.video_capture.is_opened():
        frame = self.video_capture.read()
      """
      if frame.any() != None:
        self.image_view.set_opencv_image(frame)
        self.image_view.update()
        
        self.image_view_2.set_opencv_image(frame)
        self.image_view_2.update()
        
        return True
    else:
      # If the video_capture closed, return False
      return False
    
  def load_file(self, filename):
    self.image_view_3.load(filename)
    self.set_filenamed_title(filename)
 
  def file_quit(self):
    self.terminated = True
    #self.video_capture.close()
    #self.message_queue.put("exit")
    #self.message_queue.put_nowait("exit")
    print("2")
    #sleep(5)
    #while not self.raw_video_queue.empty():
    #  frame = self.raw_video_queue.get_nowait()
    #self.close()
    print("3")
    #self.terminated = True
    
  def closeEvent(self, ce):
    self.terminated = True
    #self.video_capture.close()
    #self.message_queue.put_nowait("exit")
    print("2")
    #sleep(5)
    #while not self.raw_video_queue.empty():
    #  frame = self.raw_video_queue.get_nowait()
    #self.close()
    print("3")

####
if main(__name__):
  #if __name__ == '__main__':
  try:
    name   = os.path.basename(sys.argv[0])
    applet = ZApplication(sys.argv)
    #applet    = QApplication(sys.argv)
        
    mainv  = MainView(name, 40, 40, 640,480, device=0)

    mainv.show()
    
    p = start_cam_process(mainv.message_queue, mainv.raw_video_queue, device=0)
    
    applet.run(mainv)
    #applet.exec_()
    #applet.exec()
    print("4")
    
    p.terminate()
    #p.join()
    
    print("5")
  except:
    traceback.print_exc()