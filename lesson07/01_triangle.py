import cv2
import numpy as np

img = cv2.imread("../images/triangle.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur,100,200)

contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
# cv2.RETR_EXTERNAL εντοπίζει τα εξωτερικά περιγράμματα
# cv2.CHAIN_APPROX_NONE μας δίνει πληροφορίες για όλα τα περιγράμματα που θα εντοπίσει.

print("Σχήματα που βρήκα: ", len(contours))
area = cv2.contourArea(contours[0])
perimeter = cv2.arcLength(contours[0], True) # True για κλειστά σχήματα
print("Εμβαδόν: ", area)
print("Περίμετρος: ", perimeter)

approx = cv2.approxPolyDP(contours[0],  0.02*perimeter, True)
objCorners = len(approx)
print("Ακμές σχήματος που εντόπισα: ", objCorners)
print ("Συντεταγμένες ακμών: ", approx)

imgContour = img.copy()
cv2.drawContours(imgContour, contours[0], -1, (255, 0,0),3) # -1 για όλα τα σχήματα που εντοπίσαμε

x, y, w, h = cv2.boundingRect(approx)
cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)

if(objCorners == 3):
    objectType = "Triangle"
else:
    objectType = "Unknown"

cv2.putText(imgContour, objectType, (x + (w // 2) - 20, y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)

cv2.imshow("Input", img)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Contours", imgContour)
cv2.waitKey(0)
