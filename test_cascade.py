#import libraries
import numpy as np
import cv2

#load the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
watch_cascade = cv2.CascadeClassifier('phone_cascade.xml')

#to bring your camera feed
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    
    #convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #detect face
    faces = face_cascade.detectMultiScale(gray)
    
    #for detecting watches
    watches = watch_cascade.detectMultiScale(gray, 50, 50)
    
    #to draw rectangle on watch
    for (x,y,w,h) in watches:
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, 'Watch', (x-w, y-h), font, 0.5, (11,255,255), 3, cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    
    cv2.imshow('img', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()            