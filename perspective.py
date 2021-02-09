import cv2 as cv
import numpy as np

array = np.zeros((4,2),int)
counter = 0

def mouse_click(event,x,y,flags,para):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(image,(x,y),5,(255,0,0),3)
        array[counter] = x,y
        counter = counter + 1
        print(x,y)

image = cv.imread('9.jpg')
image = cv.resize(image,(400,500))
while True:
    if counter == 4:
        point_1 = np.float32([array[0],array[2],array[1],array[3]])
        point_2 = np.float32([[0,0],[0,500],[400,0],[400,500]])

        matrix = cv.getPerspectiveTransform(point_1,point_2)

        final = cv.warpPerspective(image,matrix,(400,500))

        cv.imshow('Warp',final)

    cv.imshow('Input',image)
    cv.setMouseCallback('Input',mouse_click)
    cv.waitKey(1)
