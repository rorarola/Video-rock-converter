import cv2
import numpy as np

cap = cv2.VideoCapture( 'test.mov')
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # always 0 in Linux python3
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # always 0 in Linux python3
print ("opencv: height:{} width:{}".format( height, width))

fourcc = cv2.VideoWriter_fourcc(*"avc1")
video_writer = cv2.VideoWriter("movie.mov", fourcc, 30.0, (width, height))


def multi_frame(frame, timer):
  pframe = cv2.resize(frame, (int(width / timer), int(height / timer)))
  frame = pframe
  for i in range(timer - 1):
    frame = np.hstack((frame, pframe))
  
  pframe = frame
  for i in range(timer - 1):
    frame = np.vstack((frame, pframe))
  return frame

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    # 寫入影格
    frame = multi_frame(frame, 6)
    video_writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

# 釋放所有資源
cap.release()
video_writer.release()
cv2.destroyAllWindows()
