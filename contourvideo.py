import cv2
video=cv2.VideoCapture('v1.mp4')
def nothing(x):
    pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar('l',"Trackbars",0,255,nothing)
cv2.createTrackbar('u',"Trackbars",0,255,nothing)
while True:
    L=cv2.getTrackbarPos('l',"Trackbars")
    U=cv2.getTrackbarPos('u',"Trackbars")
    s,f=video.read()
    f=cv2.resize(f,(400,400))
    canny=cv2.Canny(f,L,U)
    c,h=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(f,c,-1,(0,255,0),2)
    cv2.imshow('canny',canny)
    cv2.imshow('Input',f)
    cv2.waitKey(10)