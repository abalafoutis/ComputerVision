import cv2

video = cv2.VideoCapture(0)
video.set(3, 480) # Το id=3 αλλάζει το ύψος
video.set(4, 640) # το id=4 αλλάζει το πλάτος
video.set(10, 100) # το id=10 αλλάζει τη φωτεινότητα

while True:
   success, img = video.read()
   cv2.imshow("Video", img)
   if cv2.waitKey(1) & 0xFF ==  ord('q'): # Αν πατήσω το q τα τερματιστεί η επανάληψη
       break
