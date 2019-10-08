from multiprocessing import Process
from SOL4Py.opencv.ZOpenCVVideoCapture  import ZOpenCVVideoCapture
import cv2
import numpy as np
import queue
from time import time


def cam_process(raw_video_queue, device=0):
  video_capture = ZOpenCVVideoCapture()
  video_capture.open(device)
  
  # Get a raw frame
  #frame = video_capture.read()
  
  #nrows, ncols, ncs = frame.shape
  
  # Get optimal dft si
  
  # fps limit settings
  time_snapshot_seconds = time()
  fps_limit_hz = 10

  while True:
    if video_capture.is_opened():
        frame = video_capture.read()
        
        current_time_seconds = time()
        
        if current_time_seconds > time_snapshot_seconds: # Avoid dividing by zero
          if ((1/(current_time_seconds-time_snapshot_seconds)) <= fps_limit_hz): # Rate limit
            gray_image = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            #raw_video_queue.put(frame)
            raw_video_queue.put_nowait(gray_image) # non-blocking
            
            time_snapshot_seconds = current_time_seconds


def start_cam_process(raw_video_queue, device=0):
  p = Process(target=cam_process, args=(raw_video_queue, device))
  p.start()
  return p

def dft_process(to_dft_video_queue, \
                dft_settings_queue, \
                dft_magnitude_unfiltered_video_queue, \
                dft_magnitude_filtered_video_queue, \
                filtered_video_queue):
  """
  Assuming the dimensions of video frames to_dft_video_queue
  remains constant during the whole process.
  
  Assuming a video frame in to_dft_video_queue is a grayscale
  image with shape nrows, ncols .
  
  Read a first frame and determine if it should 
  be zero padded in order to have optimal
  nrows and ncols for dft speed.
  """
  to_dft_frame = to_dft_video_queue.get() # blocking
  
  nrows, ncols = to_dft_frame.shape
  
  nrows_opt, ncols_opt = cv2.getOptimalDFTSize(nrows) ,\
                         cv2.getOptimalDFTSize(ncols)
  
  if (nrows != nrows_opt) or (ncols != ncols_opt):
    adjust_dims = True
    right = ncols_opt - ncols
    bottom = nrows_opt - nrows
    bordertype = cv2.BORDER_CONSTANT
    nrows, ncols = nrows_opt, ncols_opt
  else:
    adjust_dims = False
  # Get initial settings
  dft_settings = dft_settings_queue.get() # blocking
  
  # Middle of frame (and center of centered dft)
  crow, ccol = nrows//2 , ncols//2
  
  # Start processing loop
  while True:
    # Get a frame
    to_dft_frame = to_dft_video_queue.get()
    # Shut down process if received "DONE"
    if type(to_dft_frame) == str and to_dft_frame == "DONE":
      break
    # Get new dft settings if available
    # else: Use old dft settings.
    try:
      dft_settings_new = dft_settings_queue.get_nowait() # non-blocking
      dft_settings = dft_settings_new
    except queue.Empty:
      # Using existing (previous) dft_settings
      pass
    # Zero pad frame for optimal dft speed if necessary
    if adjust_dims:
      to_dft_frame = \
      cv2.copyMakeBorder(to_dft_frame, 0, bottom, 0, right, bordertype, value = 0)
    
    # perform dft (real to complex)
    dft = cv2.dft(np.float32(to_dft_frame), flags = cv2.DFT_COMPLEX_OUTPUT)
    
    # center dft
    dft_shift = np.fft.fftshift(dft)
    
    # Magnitude spectrum in decibels
    dft_shift_magnitude = \
    20*np.log(cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))
    
    # Put the unfiltered magnitude spectrum into a sendig queue
    # for visualization.
    dft_magnitude_unfiltered_video_queue.put_nowait(dft_shift_magnitude) # non-blocking
    
    # create a mask in frequency domain for low pass filtering, 
    # center square is 1, remaining are all zeros .
    mask_frequency_domain = np.zeros((nrows, ncols, 2), np.uint8)
    mask_frequency_domain[crow-dft_settings[0]:crow+dft_settings[0], \
                          ccol-dft_settings[0]:ccol+dft_settings[0]] = 1
    
    # apply mask
    dft_shift_masked = dft_shift*mask_frequency_domain
    
    dft_shift_masked_magnitude = \
    20*np.log(cv2.magnitude(dft_shift_masked[:,:,0], dft_shift_masked[:,:,1]))
    
    # Put the filtered magnitude spectrum into a sendig queue
    # for visualization.
    dft_magnitude_filtered_video_queue.put_nowait(dft_shift_masked_magnitude) # non-blocking

    # de-center masked dft
    dft_masked = np.fft.ifftshift(dft_shift_masked)
    
    # perform inverse dft (complext to complex)
    frame_filtered_complex = cv2.idft(dft_masked)
    
    # magnitude gives the filtered image
    frame_filtered = \
    20*np.log(cv2.magnitude(frame_filtered_complex[:,:,0], frame_filtered_complex[:,:,1]))
    
    # Put the filtered frame to a queue for visualization
    filtered_video_queue.put_nowait(frame_filtered)

def start_dft_process(to_dft_video_queue, \
                      dft_settings_queue, \
                      dft_magnitude_unfiltered_video_queue, \
                      dft_magnitude_filtered_video_queue, \
                      filtered_video_queue):
  p = Process(target=dft_process, \
              args=(to_dft_video_queue, \
                    dft_settings_queue, \
                    dft_magnitude_unfiltered_video_queue, \
                    dft_magnitude_filtered_video_queue, \
                    filtered_video_queue))
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
      
      if raw_frame == "DONE":
        break
      
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
  p = Process(target=binarize_process, \
                 args=(to_binarize_video_queue, \
                       binarize_video_settings_queue, \
                       binarized_video_queue))
  p.start()
  return p
