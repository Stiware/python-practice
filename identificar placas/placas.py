from typing import Text
import cv2
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'


placa = []
imagen  = cv2.imread('descargar.jpg')
gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gray = cv2.blur(gray,(3,3))
canny = cv2.Canny(gray, 150,250)
canny = cv2.dilate(canny,None,iterations=1) 

cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)
    epsilon = 0.09*cv2.arcLength(c,True)
    approx =  cv2.approxPolyDP(c, epsilon,True)
    if len(approx)==4 and area > 9000:
        print('area=',area)
        cv2.drawContours(imagen,[c],0,(0,255,0),2)
        placa = gray[y:y+h,x:x+w]
        text = pytesseract.image_to_string(placa,config = '--psm 11')
        print('text=', text)
        cv2.imshow('placa',placa)
        cv2.moveWindow('placa',780,10)
        cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(imagen,text,(x-20,y-10),1,2.2,(0,255,0),3)



cv2.imshow('image',imagen)
#cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

