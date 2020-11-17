import cv2
import math

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if(area>500):
            print("Εμβαδόν: ", area)
            cv2.drawContours(imgContour, cnt, -1, (255, 0,0),3)
            perimeter = cv2.arcLength(cnt, True) # True για κλειστά σχήματα
            print("Περίμετρος:", perimeter)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter, True)
            print("Ακμές: ",len(approx))
            objCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if(objCorners == 3):
                objectType = "Triangle"
            elif(objCorners > 4):
                objectType = "Cirlce"
            elif(objCorners == 4):
                x0 = approx[0][0][0]
                y0 = approx[0][0][1]
                x1 = approx[1][0][0]
                y1 = approx[1][0][1]
                x2 = approx[2][0][0]
                y2 = approx[2][0][1]
                x3 = approx[3][0][0]
                y3 = approx[3][0][1]
                w1 = p2abs(x0-x1, y0-y1)
                h1 = p2abs(x0-x3, y0-y3)

                aspRatio = float(w1)/h1
                if(aspRatio > 0.95 and aspRatio < 1.05):
                    objectType = "Square"
                else:
                    objectType = "Rect"
            else:
                objectType = "Unknown"

            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType, (x+(w//2)-20, y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 2)

def p2abs(b, c):
    return math.sqrt(b ** 2 + c ** 2)

img = cv2.imread("../images/shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur,100,200)
getContours(imgCanny)

cv2.imshow("Output", imgContour)

cv2.waitKey(0)

