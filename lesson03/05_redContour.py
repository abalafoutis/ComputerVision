import cv2

img = cv2.imread("../images/lambo.png")

cv2.rectangle(img, (70,90), (500,410), (0,0,255), 2)
cv2.imshow("Red Contour", img)

cv2.rectangle(img, (70,90), (500,410), (0,0,255), cv2.FILLED)
cv2.imshow("Red Contour Filled", img)
cv2.waitKey(0)

