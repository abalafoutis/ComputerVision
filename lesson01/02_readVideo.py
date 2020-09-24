import cv2

video = cv2.VideoCapture("../videos/road.mp4")

while True:
   success, img = video.read()
   cv2.imshow("Video", img)
   cv2.waitKey(1)
