import cv2

img = cv2.imread("../images/lena.png")

cv2.imshow("Output", img)

print("Image Width: ", img.shape[1])
print("Image Height: ", img.shape[0])
print(img.shape)
<<<<<<< HEAD
cv2.waitKey(0)
=======

cv2.waitKey(0)
>>>>>>> fc88431fbd1e6c3f503f019909314f1d9ab80c06
