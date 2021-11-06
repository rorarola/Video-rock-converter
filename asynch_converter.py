import cv2
import numpy as np
import random

videoName = input('please enter your video you would like to convert: ')
timer = int(input('please enter your timer: '))
cap = cv2.VideoCapture(videoName)

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
fps = cap.get(cv2.CAP_PROP_FPS)

print ("opencv: height:{} width:{}".format( height, width))

fourcc = cv2.VideoWriter_fourcc(*"avc1")
video_writer = cv2.VideoWriter("movie.mov", fourcc, fps, (width, height))

pframes = []

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    pframes.append(cv2.resize(frame, (int(width / timer), int(height / timer))))
  else:
    break

frame_length = len(pframes)
pframes += pframes[::-1]


def row_frame():
  start = random.randint(0, frame_length - 1)
  rframes = pframes[start : start + frame_length] #第一格影片處理完畢
  
  for i in range(timer - 1):
    start = random.randint(0, frame_length - 1)
    # map(lambda(idx, frame) : {print(idx)}, enumerate(rframes))
    for j in range(frame_length):
      rframes[j] = np.hstack((rframes[j], pframes[j + start]))
  
  return rframes

result = row_frame()
for i in range(timer - 1):
  frames = row_frame()
  for j in range(frame_length):
    result[j] = np.vstack((result[j], frames[j]))


for frame in result:
  video_writer.write(frame)

# 釋放所有資源
cap.release()
video_writer.release()
cv2.destroyAllWindows()
