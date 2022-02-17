from . import finder
from .sender import *
from .defs import *
import lib
import cv2
import imutils
import time, math


# NDI-style timecode (int, 100ns resolution)
def timecode_now():
    try:
        return time.time_ns() / 100
    except:
        return int(time.time() * 1000*1000*10)

use_webcam = True
vc = None
if use_webcam:
  vc = cv2.VideoCapture(0)

sender = NDISender("SimpleSender", FourCC.BGRA)
shape = (640, 360, 4)

while(1):
  timecode = timecode_now()

  if vc and vc.isOpened():
    rval, raw_image = vc.read()
    while not rval:
        print("trying again...")
        time.sleep(1)
        rval, raw_image = vc.read()
    shape = raw_image.shape
    frame = cv2.cvtColor(raw_image, cv2.COLOR_BGR2BGRA)
  else:
    # Generate an image. Note we're working
    val = int(127.0 + 127.0*math.sin(timecode/10000000.0))
    frame = val * np.ones(shape=(shape[1], shape[0], shape[2]), dtype=np.uint8)
    frame[:, :, 0] = 255 # always full blue
    frame[:, :, 3] = 255 # set alpha to 255 (opaque)
	
  # Red text
  cv2.putText(frame, sender.name,(50,50),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 1)
  cv2.imshow("image", frame)
  sender.write(frame, timecode)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break
  
print("User Quit")
cv2.destroyAllWindows()
