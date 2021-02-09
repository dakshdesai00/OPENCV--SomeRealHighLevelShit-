import cv2
def nothing(x):
    pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar('l',"Trackbars",0,255,nothing)
cv2.createTrackbar('u',"Trackbars",0,255,nothing)
while True:
    L=cv2.getTrackbarPos('l',"Trackbars")
    U=cv2.getTrackbarPos('u',"Trackbars")
    i = cv2.imread("3.png")
    image = cv2.resize(i, (400, 400))
    canny=cv2.Canny(image,L,U)
    c,h=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image,c,-1,(0,255,0),5)
    cv2.imshow('canny',canny)
    cv2.imshow('input', image)
    cv2.waitKey(1)