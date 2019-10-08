# vid2fft
SOL4Py PyQt5 OpenCV program demonstrating 2D Discrete Fourier Transform and square filtering in frequency domain of your webcam

## Dependencies
SOL4Py-3.1 for Python3.6, PyQt5, OpenGL, OpenCV-4.1.0, ML, CNN(Keras, Torch) YOLOv3, SSD and Oracle12C (20 Sep. 2019) as specified at http://www.antillia.com/index.html

or:
```bash
conda install numpy
conda install opencv
conda install PyQt5
conda install pydotplus
conda install -c conda-forge qimage2ndarray
conda install pydot
conda install PyOpenGL
```
and likely some other packages that you will find out to be needed on your system.

## Run
```bash
python run.py
```
![](images/screenshot.PNG)

Based on https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html and example code from SOL4Py-3.1
