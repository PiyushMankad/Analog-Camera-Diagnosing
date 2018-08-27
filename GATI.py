
import cv2
import argparse
import time
import numpy
import time

### giving an arguement on the no of feeds a particular video is divided
parser=argparse.ArgumentParser()
parser.add_argument("-div","--d",type=int,default=4,help="give the no of divisions in the video feed screen ")
arg=vars(parser.parse_args())
div=arg["d"]


def notify(cam):
    global div
    if div==4 & cam==4:
        cam=3
    if div==4 & cam==5:
        cam=4
    print("Camera no{} is not working.".format(cam))


    
dvrIP='192.168.1.3'
vid=cv2.VideoCapture('rtsp://admin:admin@123@'+dvrIP+'/Streaming/Channels/01')

height = int(vid.get(3)) 
width = int(vid.get(4))   
x2=width
y2=height

if div==4:
    x1=int(width/2)
    y1=int(height/2)
if div==9:
    x1=int(width/3)
    x2=int(width*(2/3))
    y1=int(height/3)
    y2=int(height*(2/3))

while True:

    o_O,frame=vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame1=cv2.calcHist([gray[0:y1,0:x1]],[0],None,[256],[0,256])
    frame2=cv2.calcHist([gray[0:y1,x1:x2]],[0],None,[256],[0,256])
    frame3=cv2.calcHist([gray[0:y1,x2:width]],[0],None,[256],[0,256])
    frame4=cv2.calcHist([gray[y1:y2,0:x1]],[0],None,[256],[0,256])
    frame5=cv2.calcHist([gray[y1:y2,x1:x2]],[0],None,[256],[0,256])
    frame6=cv2.calcHist([gray[y1:y2,x2:width]],[0],None,[256],[0,256])
    frame7=cv2.calcHist([gray[y2:height,0:x1]],[0],None,[256],[0,256])
    frame8=cv2.calcHist([gray[y2:height,x1:x2]],[0],None,[256],[0,256])
    frame9=cv2.calcHist([gray[y2:height,x2:width]],[0],None,[256],[0,256])

    if frame9[0]>24000:
        #notify(9)
        pass
    if frame8[0]>24000:
        notify(8)
    if frame7[0]>24000:
        notify(7)
    if frame6[0]>24000:
        notify(6)
    if frame5[0]>24000:
        notify(5)
    if frame4[0]>24000:
        notify(4)
    if frame3[0]>24000:
        notify(3)
    if frame2[0]>24000:
        notify(2)
    if frame1[0]>24000:
        notify(1)

    cv2.imshow("video",gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
    

    