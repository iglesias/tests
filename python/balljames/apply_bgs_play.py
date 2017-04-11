#!/usr/bin/python

import sys
import cv2

if len(sys.argv) < 2:
  print 'Usage: ./apply_bgs_play.py [VIDEO]'
  sys.exit(1)

video_capture = cv2.VideoCapture(sys.argv[1])
if not video_capture.isOpened():
  print 'Video file could not be opened.'
  sys.exit(1)

# If the frame size is too large for the monitor, we can resize the window.
cv2.namedWindow('Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Window', int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)/2),
                 int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)/2))

num_frames = video_capture.get(cv2.CAP_PROP_FRAME_COUNT)
knn = cv2.createBackgroundSubtractorKNN()
frame_idx = 0
while frame_idx < num_frames:
  ret, frame = video_capture.read()
  frame_idx += 1

  if not ret:
    print 'Frame %d could not be read properly.' % frame_idx
    sys.exit(1)

  bgs_frame = knn.apply(frame, 0)

  cv2.putText(bgs_frame, str(frame_idx), (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 2,
              (255, 255, 255))

  cv2.imshow('Window', bgs_frame)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cv2.destroyAllWindows()
