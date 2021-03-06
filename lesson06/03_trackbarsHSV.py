import cv2
import numpy as np

def empty(a):
   pass

img = cv2.imread("../images/lambo.png")
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 359, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 0, 359, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 0, 255, empty)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
   h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
   h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
   s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
   s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
   v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
   v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
   print(h_min,h_max,s_min,s_max,v_min,v_max)
   cv2.waitKey(1000)
   cv2.imshow("Image", img)
   cv2.imshow("Image HSV", imgHSV)
   cv2.waitKey(1)
