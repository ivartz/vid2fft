import multiprocessing as mp
from SOL4Py.opencv.ZOpenCVVideoCapture  import ZOpenCVVideoCapture
import cv2


def cam_process(raw_video_queue, device=0):
  video_capture = ZOpenCVVideoCapture()
  video_capture.open(device)
  while True:
    if video_capture.is_opened():
        frame = video_capture.read()
        #raw_video_queue.put(frame)
        raw_video_queue.put_nowait(frame) # non-blocking


def start_cam_process(raw_video_queue, device=0):
  p = mp.Process(target=cam_process, args=(raw_video_queue, device))
  p.start()
  return p

def binarize_process(to_binarize_video_queue, \
                     binarize_video_settings_queue, \
                     binarized_video_queue):
  binarize_settings = None
  #binarize_settings = (11, 0, 0)
  while True:
    if (not binarize_video_settings_queue.empty()) and (binarize_settings == None):
      binarize_settings = binarize_video_settings_queue.get() # blocking
    elif (not binarize_video_settings_queue.empty()) and (binarize_settings != None):
      binarize_settings = binarize_video_settings_queue.get() # blocking
    if (not to_binarize_video_queue.empty()) and (binarize_settings != None):
      raw_frame = to_binarize_video_queue.get() # blocking
      
      if raw_frame.any() != None:
        gray_image = cv2.cvtColor(raw_frame, cv2.COLOR_RGB2GRAY)
        MAX_PIXEL_VALUE    = 255
        C                  = 9.0
        adaptive_method_id = binarize_settings[0]
        threshold_type_id  = binarize_settings[1]
        block_size         = binarize_settings[2]
        binarized_image    = cv2.adaptiveThreshold(gray_image, \
                                                   MAX_PIXEL_VALUE, \
                                                   adaptive_method_id, \
                                                   threshold_type_id, \
                                                   block_size, \
                                                   C);
        binarized_video_queue.put_nowait(binarized_image) # non-blocking

def start_binarize_process(to_binarize_video_queue, \
                           binarize_video_settings_queue, \
                           binarized_video_queue):
  p = mp.Process(target=binarize_process, \
                 args=(to_binarize_video_queue, \
                       binarize_video_settings_queue, \
                       binarized_video_queue))
  p.start()
  return p
