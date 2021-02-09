import cv2
image=cv2.imread('2.jpg')
i=cv2.resize(image,(500,500))
# for rect
cv2.rectangle(i,(60,120),(190,220),(0,255,0),4)
cv2.rectangle(i,(300,120),(425,220),(0,255,0),4)
cv2.circle(i,(99,162),8,(0,255,0),4)
cv2.circle(i,(158,162),8,(0,255,0),4)
cv2.circle(i,(345,168),8,(0,255,0),4)
cv2.circle(i,(383,162),8,(0,255,0),4)
cv2.putText(i,"CHUNU",(60,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),4)
cv2.putText(i,"MUNU",(300,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),4)
cv2.imshow('Output',i)

print(i.shape)
cv2.waitKey(0)
