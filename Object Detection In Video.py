import cv2
import numpy as np
video=cv2.VideoCapture('1.mp4')#capturing video

while True:#runnig code inside in loop
    s,f = video.read()#reading video
    f = cv2.resize(f, (400, 400))# resizing video
    cv2.imshow('Original Video', f)#displaying original video tab
    blue_lower = np.array([85, 75, 1])#lowest value of blue color
    blue_upper=np.array([125, 255, 255])#highest value of blue color
    mask=cv2.inRange(f,blue_lower,blue_upper)#bringing blue_lower and blue_upper in video
    final_result = cv2.bitwise_not(f, f, mask=mask)#merging both arrays
    c,h=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#it find contours
    cv2.drawContours(f,c,-1,(0,0,255),5)#it draws contours
    cv2.imshow('Object Detected', final_result)#showing object detected
    cv2.waitKey(20)#runnig video