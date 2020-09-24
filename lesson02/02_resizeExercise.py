# Τι θα συμβεί αν εκτελέσω τις παρακάτω λειτουργίες:
#    - Διαβάσω την εικόνα lambo.png
#    - Αλλάξω το μέγεθος της εικόνας σε (300,200)
#    - Αλλάξω ξανά την προηγούμενη εικόνα στο αρχικό της μέγεθος

import cv2

img = cv2.imread("../images/lambo.png")
print(img.shape)

imgResize = cv2.resize(img, (300, 200))  # Πρώτα ορίζω το νέο πλάτος και μετά το νέο ύψος
print(imgResize.shape)

imgResize2 = cv2.resize(imgResize, (623, 462))

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Resize2", imgResize2)
cv2.waitKey(0)


