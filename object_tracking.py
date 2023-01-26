import cv2
import math
import time

p1=530
p2=300

vid=cv2.VideoCapture('footvolleyball.mp4')
tracker=cv2.TrackerCSRT_create()

check,img=vid.read()

box=cv2.selectROI('tracking',img,False)
tracker.init(img,box)
print(box)

def drawBox(img,box):
    x,y,w,h=int(box[0]),int(box[1]),int(box[2]),int(box[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(img,'tracking',(100,100),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

def goalTrack(img,box):
    x,y,w,h=int(box[0]),int(box[1]),int(box[2]),int(box[3])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(img,(c1,c2),2,(0,255,0),3)
    cv2.circle(img,(int(p1),int(p2)),2,(255,0,255),3)
    
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)

while True:
    ret,img=vid.read()
    check,box=tracker.update(img)
    if(check):
        drawBox(img,box)
    else:
        cv2.putText(img,'lost',(100,100),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
       
    goalTrack(img,box) 
    cv2.imshow('result',img)
    if(cv2.waitKey(25)==32):
        break

vid.release()
cv2.destroyAllWindows()

