import cv2

img = cv2.imread("../images/lena.png")

cv2.imshow("Output", img)

print("Image Width: ", img.shape[1])
print("Image Height: ", img.shape[0])
print(img.shape)
cv2.waitKey(0)