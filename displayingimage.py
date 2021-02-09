import cv2
image=cv2.imread('ironman_PNG74.png')
i=cv2.resize(image,(500,500))
# for rect
cv2.rectangle(i,(190,0),(290,110),(0,255,0),4)
cv2.rectangle(i,(205,60),(235,75),(0,255,0),4)
cv2.rectangle(i,(250,60),(280,75),(0,255,0),4)
cv2.putText(i,"IRON MAN",(50,90),cv2.FONT_ITALIC,1,(0,0,0),4)
#for circle
cv2.circle(i,(58,125),(20),(0,255,0),10)
cv2.circle(i,(305,170),(20),(0,255,0),10)
cv2.imshow('Output',i)

print(i.shape)
cv2.waitKey(0)
