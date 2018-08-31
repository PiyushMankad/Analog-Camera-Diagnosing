
import cv2
import argparse
import time
import numpy
import time
import sys

parser=argparse.ArgumentParser()
parser.add_argument("-channels","--ch",type=int,default=4,help="give the no of divisions in the video feed screen ")
arg=vars(parser.parse_args())
channel=arg["ch"]
print(channel)

    
dvrIP='192.168.1.3'
vid=cv2.VideoCapture('rtsp://admin:admin@123@'+dvrIP+'/Streaming/Channels/01')

height = int(vid.get(3)) 
width = int(vid.get(4))   


def notify(cam):
    print("Camera no{} is not working.".format(cam))

def ch4dvr():
    global vid
    global width
    global height

    x1=int(width/2)
    y1=int(height/2)

    o_O,frame=vid.read()

    if o_O==False:
        print("DVR is not working...Check Connections")
    else:    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        frame1=cv2.calcHist([gray[0:y1,0:x1]],[0],None,[256],[0,256])
        frame2=cv2.calcHist([gray[0:y1,x1:width]],[0],None,[256],[0,256])
        frame3=cv2.calcHist([gray[y1:height,0:x1]],[0],None,[256],[0,256])
        frame4=cv2.calcHist([gray[y1:height,x1:width]],[0],None,[256],[0,256])

        if frame4[0]>24000:
            notify(4)
        if frame3[0]>24000:
            notify(3)
        if frame2[0]>24000:
            notify(2)
        if frame1[0]>24000:
            notify(1)

def ch8dvr():
    global vid
    global width
    global height

    x1=int(width/3)
    x2=int(width*(2/3))
    y1=int(height/3)
    y2=int(height*(2/3))
    
    o_O,frame=vid.read()
    if o_O==False:
        print("DVR is not working...Check Connections")
        
    else:    
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

def ch16dvr():
    global vid
    global width
    global height

    x1=int(width/4)
    x2=int(width*(2/4))
    x3=int(width*(3/4))
    y1=int(height/4)
    y2=int(height*(2/4))
    y3=int(height*(3/4))

    o_O,frame=vid.read()
    if o_O==False:
        print("DVR is not working...Check Connections")
    else:    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        frame1=cv2.calcHist([gray[0:y1,0:x1]],[0],None,[256],[0,256])
        frame2=cv2.calcHist([gray[0:y1,x1:x2]],[0],None,[256],[0,256])
        frame3=cv2.calcHist([gray[0:y1,x2:x3]],[0],None,[256],[0,256])
        frame4=cv2.calcHist([gray[0:y1,x3:width]],[0],None,[256],[0,256])
        frame5=cv2.calcHist([gray[y1:y2,0:x1]],[0],None,[256],[0,256])
        frame6=cv2.calcHist([gray[y1:y2,x1:x2]],[0],None,[256],[0,256])
        frame7=cv2.calcHist([gray[y1:y2,x2:x3]],[0],None,[256],[0,256])
        frame8=cv2.calcHist([gray[y1:y2,x3:width]],[0],None,[256],[0,256])
        frame9=cv2.calcHist([gray[y3:y3,0:x1]],[0],None,[256],[0,256])
        frame10=cv2.calcHist([gray[y3:y3,x1:x2]],[0],None,[256],[0,256])
        frame11=cv2.calcHist([gray[y3:y3,x2:x3]],[0],None,[256],[0,256])
        frame12=cv2.calcHist([gray[y3:y3,x3:width]],[0],None,[256],[0,256])
        frame13=cv2.calcHist([gray[y3:height,0:x1]],[0],None,[256],[0,256])
        frame14=cv2.calcHist([gray[y3:height,x1:x2]],[0],None,[256],[0,256])
        frame15=cv2.calcHist([gray[y3:height,x2:x3]],[0],None,[256],[0,256])
        frame16=cv2.calcHist([gray[y3:height,x3:width]],[0],None,[256],[0,256])
        
        if frame16[0]>8000:
            notify(16)
        if frame15[0]>8000:
            notify(15)
        if frame14[0]>8000:
            notify(14)
        if frame13[0]>8000:
            notify(13)
        if frame12[0]>8000:
            notify(12)
        if frame11[0]>8000:
            notify(11)
        if frame10[0]>8000:
            notify(10)
        if frame9[0]>8000:
            notify(9)
        if frame8[0]>8000:
            notify(8)
        if frame7[0]>8000:
            notify(7)
        if frame6[0]>8000:
            notify(6)
        if frame5[0]>8000:
            notify(5)
        if frame4[0]>8000:
            notify(4)
        if frame3[0]>8000:
            notify(3)
        if frame2[0]>8000:
            notify(2)
        if frame1[0]>8000:
            notify(1)

def ch24dvr():
    global vid
    global width
    global height

    x1=int(width/5)
    x2=int(width*(2/5))
    x3=int(width*(3/5))
    x4=int(width*(4/5))
    y1=int(height/5)
    y2=int(height*(2/5))
    y3=int(height*(3/5))
    y4=int(height*(4/5))

    o_O,frame=vid.read()
    if o_O==False:
        print("DVR is not working...Check Connections")
    else:    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        frame1=cv2.calcHist([gray[0:y1,0:x1]],[0],None,[256],[0,256])
        frame2=cv2.calcHist([gray[0:y1,x1:x2]],[0],None,[256],[0,256])
        frame3=cv2.calcHist([gray[0:y1,x2:x3]],[0],None,[256],[0,256])
        frame4=cv2.calcHist([gray[0:y1,x3:x4]],[0],None,[256],[0,256])
        frame5=cv2.calcHist([gray[0:y1,x4:width]],[0],None,[256],[0,256])
        frame6=cv2.calcHist([gray[y1:y2,0:x1]],[0],None,[256],[0,256])
        frame7=cv2.calcHist([gray[y1:y2,x1:x2]],[0],None,[256],[0,256])
        frame8=cv2.calcHist([gray[y1:y2,x2:x3]],[0],None,[256],[0,256])
        frame9=cv2.calcHist([gray[y1:y2,x3:x4]],[0],None,[256],[0,256])
        frame10=cv2.calcHist([gray[y1:y2,x4:width]],[0],None,[256],[0,256])
        frame11=cv2.calcHist([gray[y2:y3,0:x1]],[0],None,[256],[0,256])
        frame12=cv2.calcHist([gray[y2:y3,x1:x2]],[0],None,[256],[0,256])
        frame13=cv2.calcHist([gray[y2:y3,x2:x3]],[0],None,[256],[0,256])
        frame14=cv2.calcHist([gray[y2:y3,x3:x4]],[0],None,[256],[0,256])
        frame15=cv2.calcHist([gray[y2:y3,x4:width]],[0],None,[256],[0,256])
        frame16=cv2.calcHist([gray[y3:y4,0:x1]],[0],None,[256],[0,256])
        frame17=cv2.calcHist([gray[y3:y4,x1:x2]],[0],None,[256],[0,256])
        frame18=cv2.calcHist([gray[y3:y4,x2:x3]],[0],None,[256],[0,256])
        frame19=cv2.calcHist([gray[y3:y4,x3:x4]],[0],None,[256],[0,256])
        frame20=cv2.calcHist([gray[y3:y4,x4:width]],[0],None,[256],[0,256])
        frame21=cv2.calcHist([gray[y4:height,0:x1]],[0],None,[256],[0,256])
        frame22=cv2.calcHist([gray[y4:height,x1:x2]],[0],None,[256],[0,256])
        frame23=cv2.calcHist([gray[y4:height,x2:x3]],[0],None,[256],[0,256])
        frame24=cv2.calcHist([gray[y4:height,x3:x4]],[0],None,[256],[0,256])
        frame25=cv2.calcHist([gray[y4:height,x4:width]],[0],None,[256],[0,256])
        
        if frame24[0]>2600:
            notify(24)
        if frame23[0]>2600:
            notify(23)
        if frame22[0]>2600:
            notify(22)
        if frame21[0]>2600:
            notify(21)
        if frame20[0]>2600:
            notify(20)
        if frame19[0]>2600:
            notify(19)
        if frame18[0]>2600:
            notify(18)
        if frame17[0]>2600:
            notify(17)
        if frame16[0]>2600:
            notify(16)
        if frame15[0]>2600:
            notify(15)
        if frame14[0]>2600:
            notify(14)
        if frame13[0]>2600:
            notify(13)
        if frame12[0]>2600:
            notify(12)
        if frame11[0]>2600:
            notify(11)
        if frame10[0]>2600:
            notify(10)
        if frame9[0]>2600:
            notify(9)
        if frame8[0]>2600:
            notify(8)
        if frame7[0]>2600:
            notify(7)
        if frame6[0]>2600:
            notify(6)
        if frame5[0]>2600:
            notify(5)
        if frame4[0]>2600:
            notify(4)
        if frame3[0]>2600:
            notify(3)
        if frame2[0]>2600:
            notify(2)
        if frame1[0]>2600:
            notify(1)

### ch32dvr has to be setted with histograms ###
def ch32dvr():
    global vid
    global width
    global height

    x1=int(width/6)
    x2=int(width*(2/6))
    x3=int(width*(3/6))
    x4=int(width*(4/6))
    x5=int(width*(5/6))
    y1=int(height/6)
    y2=int(height*(2/6))
    y3=int(height*(3/6))
    y4=int(height*(4/6))
    y5=int(height*(5/6))

    o_O,frame=vid.read()
    if o_O==False:
        print("DVR is not working...Check Connections")
    else:    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        frame1=cv2.calcHist([gray[y2:y4,x2:x4]],[0],None,[256],[0,256])###GOLDEN####
        frame2=cv2.calcHist([gray[0:y1,x1:x2]],[0],None,[256],[0,256])
        frame3=cv2.calcHist([gray[0:y1,x2:x3]],[0],None,[256],[0,256])
        frame4=cv2.calcHist([gray[0:y1,x3:x4]],[0],None,[256],[0,256])
        frame5=cv2.calcHist([gray[0:y1,x4:x5]],[0],None,[256],[0,256])
        frame6=cv2.calcHist([gray[0:y1,x5:width]],[0],None,[256],[0,256])

        frame7=cv2.calcHist([gray[y1:y2,0:x1]],[0],None,[256],[0,256])
        frame8=cv2.calcHist([gray[y1:y2,x1:x2]],[0],None,[256],[0,256])
        frame9=cv2.calcHist([gray[y1:y2,x2:x3]],[0],None,[256],[0,256])
        frame10=cv2.calcHist([gray[y1:y2,x3:x4]],[0],None,[256],[0,256])
        frame11=cv2.calcHist([gray[y1:y2,x4:x5]],[0],None,[256],[0,256])
        frame12=cv2.calcHist([gray[y1:y2,x5:width]],[0],None,[256],[0,256])

        frame13=cv2.calcHist([gray[y2:y3,0:x1]],[0],None,[256],[0,256])
        frame14=cv2.calcHist([gray[y2:y3,x1:x2]],[0],None,[256],[0,256])
        frame15=cv2.calcHist([gray[y2:y3,x4:x5]],[0],None,[256],[0,256])
        frame16=cv2.calcHist([gray[y2:y3,x5:width]],[0],None,[256],[0,256])

        frame17=cv2.calcHist([gray[y3:y4,0:x1]],[0],None,[256],[0,256])
        frame18=cv2.calcHist([gray[y3:y4,x1:x2]],[0],None,[256],[0,256])
        frame19=cv2.calcHist([gray[y3:y4,x4:x5]],[0],None,[256],[0,256])
        frame20=cv2.calcHist([gray[y3:y4,x5:width]],[0],None,[256],[0,256])

        frame21=cv2.calcHist([gray[y4:y5,0:x1]],[0],None,[256],[0,256])
        frame22=cv2.calcHist([gray[y4:y5,x1:x2]],[0],None,[256],[0,256])
        frame23=cv2.calcHist([gray[y4:y5,x2:x3]],[0],None,[256],[0,256])
        frame24=cv2.calcHist([gray[y4:y5,x3:x4]],[0],None,[256],[0,256])
        frame25=cv2.calcHist([gray[y4:y5,x4:x5]],[0],None,[256],[0,256])
        frame26=cv2.calcHist([gray[y4:y5,x5:width]],[0],None,[256],[0,256])
        frame27=cv2.calcHist([gray[y5:height,0:x1]],[0],None,[256],[0,256])
        frame28=cv2.calcHist([gray[y5:height,x1:x2]],[0],None,[256],[0,256])
        frame29=cv2.calcHist([gray[y5:height,x2:x3]],[0],None,[256],[0,256])
        frame30=cv2.calcHist([gray[y5:height,x3:x4]],[0],None,[256],[0,256])
        frame31=cv2.calcHist([gray[y5:height,x4:x5]],[0],None,[256],[0,256])
        frame32=cv2.calcHist([gray[y5:height,x5:width]],[0],None,[256],[0,256])

        if frame32[0]>880:
            notify(32)
        if frame31[0]>880:
            notify(31)
        if frame30[0]>880:
            notify(30)
        if frame29[0]>880:
            notify(29)
        if frame28[0]>880:
            notify(28)
        if frame27[0]>880:
            notify(27)
        if frame26[0]>880:
            notify(26)
        if frame25[0]>880:
            notify(25)
        if frame24[0]>880:
            notify(24)
        if frame23[0]>880:
            notify(23)
        if frame22[0]>880:
            notify(22)
        if frame21[0]>880:
            notify(21)
        if frame20[0]>880:
            notify(20)
        if frame19[0]>880:
            notify(19)
        if frame18[0]>880:
            notify(18)
        if frame17[0]>880:
            notify(17)
        if frame16[0]>880:
            notify(16)
        if frame15[0]>880:
            notify(15)
        if frame14[0]>880:
            notify(14)
        if frame13[0]>880:
            notify(13)
        if frame12[0]>880:
            notify(12)
        if frame11[0]>880:
            notify(11)
        if frame10[0]>880:
            notify(10)
        if frame9[0]>880:
            notify(9)
        if frame8[0]>880:
            notify(8)
        if frame7[0]>880:
            notify(7)
        if frame6[0]>880:
            notify(6)
        if frame5[0]>880:
            notify(5)
        if frame4[0]>880:
            notify(4)
        if frame3[0]>880:
            notify(3)
        if frame2[0]>880:
            notify(2)
        if frame1[0]>24000:
            notify(1)

### ch48dvr has to be setted with histograms ###
def ch48dvr():
    global vid
    global width
    global height

    x1=int(width/7)
    x2=int(width*(2/7))
    x3=int(width*(3/7))
    x4=int(width*(4/7))
    x5=int(width*(5/7))
    x6=int(width*(6/7))
    y1=int(height/7)
    y2=int(height*(2/7))
    y3=int(height*(3/7))
    y4=int(height*(4/7))
    y5=int(height*(5/7))
    y6=int(height*(6/7))
        
    o_O,frame=vid.read()
    if o_O==False:
        print("DVR is not working...Check Connections")
    else:    
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        frame1=cv2.calcHist([gray[0:y1,0:x1]],[0],None,[256],[0,256])
        frame2=cv2.calcHist([gray[0:y1,x1:x2]],[0],None,[256],[0,256])
        frame3=cv2.calcHist([gray[0:y1,x2:x3]],[0],None,[256],[0,256])
        frame4=cv2.calcHist([gray[0:y1,x3:x4]],[0],None,[256],[0,256])
        frame5=cv2.calcHist([gray[0:y1,x4:x5]],[0],None,[256],[0,256])
        frame6=cv2.calcHist([gray[0:y1,x5:x6]],[0],None,[256],[0,256])
        frame7=cv2.calcHist([gray[0:y1,x6:width]],[0],None,[256],[0,256])
        frame8=cv2.calcHist([gray[y1:y2,0:x1]],[0],None,[256],[0,256])
        frame9=cv2.calcHist([gray[y1:y2,x1:x2]],[0],None,[256],[0,256])
        frame10=cv2.calcHist([gray[y1:y2,x2:x3]],[0],None,[256],[0,256])
        frame11=cv2.calcHist([gray[y1:y2,x3:x4]],[0],None,[256],[0,256])
        frame12=cv2.calcHist([gray[y1:y2,x4:x5]],[0],None,[256],[0,256])
        frame13=cv2.calcHist([gray[y1:y2,x5:x6]],[0],None,[256],[0,256])
        frame14=cv2.calcHist([gray[y1:y2,x6:width]],[0],None,[256],[0,256])
        frame15=cv2.calcHist([gray[y2:y3,0:x1]],[0],None,[256],[0,256])
        frame16=cv2.calcHist([gray[y2:y3,x1:x2]],[0],None,[256],[0,256])
        frame17=cv2.calcHist([gray[y2:y3,x2:x3]],[0],None,[256],[0,256])
        frame18=cv2.calcHist([gray[y2:y3,x3:x4]],[0],None,[256],[0,256])
        frame19=cv2.calcHist([gray[y2:y3,x4:x5]],[0],None,[256],[0,256])
        frame20=cv2.calcHist([gray[y2:y3,x5:x6]],[0],None,[256],[0,256])
        frame21=cv2.calcHist([gray[y2:y3,x6:width]],[0],None,[256],[0,256])
        frame22=cv2.calcHist([gray[y3:y4,0:x1]],[0],None,[256],[0,256])
        frame23=cv2.calcHist([gray[y3:y4,x1:x2]],[0],None,[256],[0,256])
        frame24=cv2.calcHist([gray[y3:y4,x2:x3]],[0],None,[256],[0,256])
        frame25=cv2.calcHist([gray[y3:y4,x3:x4]],[0],None,[256],[0,256])
        frame26=cv2.calcHist([gray[y3:y4,x4:x5]],[0],None,[256],[0,256])
        frame27=cv2.calcHist([gray[y3:y4,x5:x6]],[0],None,[256],[0,256])
        frame28=cv2.calcHist([gray[y3:y4,x6:width]],[0],None,[256],[0,256])
        frame29=cv2.calcHist([gray[y4:y5,0:x1]],[0],None,[256],[0,256])
        frame30=cv2.calcHist([gray[y4:y5,x1:x2]],[0],None,[256],[0,256])
        frame31=cv2.calcHist([gray[y4:y5,x2:x3]],[0],None,[256],[0,256])
        frame32=cv2.calcHist([gray[y4:y5,x3:x4]],[0],None,[256],[0,256])
        frame33=cv2.calcHist([gray[y4:y5,x4:x5]],[0],None,[256],[0,256])
        frame34=cv2.calcHist([gray[y4:y5,x5:x6]],[0],None,[256],[0,256])
        frame35=cv2.calcHist([gray[y4:y5,x6:width]],[0],None,[256],[0,256])
        frame36=cv2.calcHist([gray[y5:y6,0:x1]],[0],None,[256],[0,256])
        frame37=cv2.calcHist([gray[y5:y6,x1:x2]],[0],None,[256],[0,256])
        frame38=cv2.calcHist([gray[y5:y6,x2:x3]],[0],None,[256],[0,256])
        frame39=cv2.calcHist([gray[y5:y6,x3:x4]],[0],None,[256],[0,256])
        frame40=cv2.calcHist([gray[y5:y6,x4:x5]],[0],None,[256],[0,256])
        frame41=cv2.calcHist([gray[y5:y6,x5:x6]],[0],None,[256],[0,256])
        frame42=cv2.calcHist([gray[y5:y6,x6:width]],[0],None,[256],[0,256])
        frame43=cv2.calcHist([gray[y6:height,0:x1]],[0],None,[256],[0,256])
        frame44=cv2.calcHist([gray[y6:height,x1:x2]],[0],None,[256],[0,256])
        frame45=cv2.calcHist([gray[y6:height,x2:x3]],[0],None,[256],[0,256])
        frame46=cv2.calcHist([gray[y6:height,x3:x4]],[0],None,[256],[0,256])
        frame47=cv2.calcHist([gray[y6:height,x4:x5]],[0],None,[256],[0,256])
        frame48=cv2.calcHist([gray[y6:height,x5:x6]],[0],None,[256],[0,256])
        frame49=cv2.calcHist([gray[y6:height,x6:width]],[0],None,[256],[0,256])

        if frame48[0]>880:
            notify(48)
        if frame47[0]>880:
            notify(47)
        if frame46[0]>880:
            notify(46)
        if frame45[0]>880:
            notify(45)
        if frame44[0]>880:
            notify(44)
        if frame43[0]>880:
            notify(43)
        if frame42[0]>880:
            notify(42)
        if frame41[0]>880:
            notify(41)
        if frame40[0]>880:
            notify(40)
        if frame39[0]>880:
            notify(39)
        if frame38[0]>880:
            notify(38)
        if frame37[0]>880:
            notify(37)
        if frame36[0]>880:
            notify(36)
        if frame35[0]>880:
            notify(35)
        if frame34[0]>880:
            notify(34)
        if frame33[0]>880:
            notify(33)
        if frame32[0]>880:
            notify(32)
        if frame31[0]>880:
            notify(31)
        if frame30[0]>880:
            notify(30)
        if frame29[0]>880:
            notify(29)
        if frame28[0]>880:
            notify(28)
        if frame27[0]>880:
            notify(27)
        if frame26[0]>880:
            notify(26)
        if frame25[0]>880:
            notify(25)
        if frame24[0]>880:
            notify(24)
        if frame23[0]>880:
            notify(23)
        if frame22[0]>880:
            notify(22)
        if frame21[0]>880:
            notify(21)
        if frame20[0]>880:
            notify(20)
        if frame19[0]>880:
            notify(19)
        if frame18[0]>880:
            notify(18)
        if frame17[0]>880:
            notify(17)
        if frame16[0]>880:
            notify(16)
        if frame15[0]>880:
            notify(15)
        if frame14[0]>880:
            notify(14)
        if frame13[0]>880:
            notify(13)
        if frame12[0]>880:
            notify(12)
        if frame11[0]>880:
            notify(11)
        if frame10[0]>880:
            notify(10)
        if frame9[0]>880:
            notify(9)
        if frame8[0]>880:
            notify(8)
        if frame7[0]>880:
            notify(7)
        if frame6[0]>880:
            notify(6)
        if frame5[0]>880:
            notify(5)
        if frame4[0]>880:
            notify(4)
        if frame3[0]>880:
            notify(3)
        if frame2[0]>880:
            notify(2)
        if frame1[0]>880:
            notify(1)

def number_of_channels(argument):
    switcher = {
        4: ch4dvr,
        8: ch8dvr,
        16: ch16dvr,
        24: ch24dvr,
        32: ch32dvr,
        48: ch48dvr,
    }
    func = switcher.get(argument, lambda: "DVR is invalid")
    func()

number_of_channels(channel)