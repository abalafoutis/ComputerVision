import cv2

def empty(a):
   pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("variable X", "TrackBars", 0, 255, empty)
cv2.createTrackbar("variable Y", "TrackBars", 20, 255, empty)
cv2.createTrackbar("variable Z", "TrackBars", 50, 255, empty)

while True:
   x = cv2.getTrackbarPos("variable X", "TrackBars")
   y = cv2.getTrackbarPos("variable Y", "TrackBars")
   z = cv2.getTrackbarPos("variable Z", "TrackBars")
   print(x,y,z)
   cv2.waitKey(1000)