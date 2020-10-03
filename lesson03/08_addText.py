import cv2

img = cv2.imread("../images/lena.png")

cv2.circle(img, (270,266), 20, (0,0,0), 3)
cv2.circle(img, (330,266), 20, (0,0,0), 3)
cv2.line(img, (290, 266), (310, 266),(0,0,0), 3)

cv2.putText(img, "Lena with glasses", (70,40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)


