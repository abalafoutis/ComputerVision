import cv2

img = cv2.imread("../images/lambo.png")
print(img.shape)

imgCropped = img[0:200, 250:500]   # Πρώτη παράμετρος το ύψος, δεύτερη το πλάτος
print(imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)


