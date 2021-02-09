import cv2

def nothing(x):
    pass


cv2.namedWindow("output")
cv2.createTrackbar("Treshold_min","output",0,255,nothing)
cv2.createTrackbar("Treshold_max","output",0,255,nothing)
cv2.createTrackbar("Swift","output",0,1,nothing)
while True:

    i = cv2.imread("3.png")
    image=cv2.resize(i,(500,500))
    tmi=cv2.getTrackbarPos("Treshold_min","output")
    tma=cv2.getTrackbarPos("Treshold_max","output")
    z = cv2.getTrackbarPos("Swift", "output")
    if z==1:
        ed = cv2.Canny(image, tmi, tma)
        cv2.imshow('output', ed)
        cv2.imshow('Input', image)
    else:
        pass

    cv2.waitKey(1)