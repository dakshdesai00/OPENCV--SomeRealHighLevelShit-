import cv2 as cv
import numpy as np
def nothing(x):
    pass
cv.namedWindow('Trackbars')
cv.createTrackbar("Hue_min","Trackbars",0,179,nothing)
cv.createTrackbar("Hue_max","Trackbars",179,179,nothing)
cv.createTrackbar("Sat_min","Trackbars",0,255,nothing)
cv.createTrackbar("Sat_max","Trackbars",255,255,nothing)
cv.createTrackbar("Value_min","Trackbars",0,255,nothing)
cv.createTrackbar("Value_max","Trackbars",255,255,nothing)
while True:
    image = cv.imread('4.jpg')
    i = cv.resize(image, (250, 250))

    hmin=cv.getTrackbarPos("Hue_min","Trackbars")
    hmax = cv.getTrackbarPos("Hue_max", "Trackbars")
    smin = cv.getTrackbarPos("Sat_min", "Trackbars")
    smax = cv.getTrackbarPos("Sat_max", "Trackbars")
    vmin = cv.getTrackbarPos("Value_min", "Trackbars")
    vmax = cv.getTrackbarPos("Value_max", "Trackbars")
    #print(hmin,hmax,smin,smax,vmin,vmax)
    lower=np.array([hmin,smin,vmin])
    upper=np.array([hmax,smax,vmax])
    mask=cv.inRange(i,lower,upper)
    cv.imshow('Input', i)
    final_result=cv.bitwise_not(i,i,mask=mask)

    cv.imshow('Output',mask)

    cv.imshow('FinalResult',final_result)
    cv.waitKey(1)

