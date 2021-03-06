from tkinter import *
import tkinter as tkinter
import cv2
import time 
import sys
from functools import partial

#path=""
msg=[None]*50

def do():
	print(channel.get())

def notify(cam):
	global msg
	#print("Camera no"+str(cam)+" is not working.")
	msg[cam]="Camera no"+str(cam)+" is not working."

def ch4dvr():
    global vid
    global width
    global height
    global msg

    x1=int(width/2)
    y1=int(height/2)

    o_O,frame=vid.read()

    if o_O==False:
        print("DVR is not working...Check Connections")
        msg[49]="DVR is not working...Check Connections"
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
    global msg

    x1=int(width/3)
    x2=int(width*(2/3))
    y1=int(height/3)
    y2=int(height*(2/3))
    
    o_O,frame=vid.read()
    if o_O==False:
        print("DVR is not working...Check Connections")
        msg[49]="DVR is not working...Check Connections"
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
    global msg

    x1=int(width/4)
    x2=int(width*(2/4))
    x3=int(width*(3/4))
    y1=int(height/4)
    y2=int(height*(2/4))
    y3=int(height*(3/4))

    o_O,frame=vid.read()
    if o_O==False:
        print("DVR is not working...Check Connections")
        msg[49]="DVR is not working...Check Connections"
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
    global msg

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
        msg[49]="DVR is not working...Check Connections"
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
    global msg

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
        msg[49]="DVR is not working...Check Connections"
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
    global msg

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
        msg[49]="DVR is not working...Check Connections"
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

def number_of_channels(argument,user,password,dvr):
    global path
    global vid
    global height
    global width
    global msg

    msg=[None]*50
    path='rtsp://'+str(user.get())+':'+str(password.get())+'@'+str(dvr.get())+'/Streaming/Channels/01'
    vid=cv2.VideoCapture(path)
    height = int(vid.get(3))
    width = int(vid.get(4)) 

    switcher = {
        4: ch4dvr,
        8: ch8dvr,
        16: ch16dvr,
        24: ch24dvr,
        32: ch32dvr,
        48: ch48dvr,
    }

    func = switcher.get(int(argument.get()), lambda: "DVR is invalid")
    func()

    notif=Frame(root,bd=7,height=100,width=100,relief="groove")
    heading=Label(notif,text="Notifications",fg="white",bg="black", font = 'Verdana 14 bold').grid(row=0,column=0,columnspan=5,sticky=W+E,pady=20,padx=10)
    lbl1=Label(notif,text=msg[1]).grid(row=1,column=0)
    lbl2=Label(notif,text=msg[2]).grid(row=2,column=0)
    lbl3=Label(notif,text=msg[3]).grid(row=3,column=0)
    lbl4=Label(notif,text=msg[4]).grid(row=4,column=0)
    lbl5=Label(notif,text=msg[5]).grid(row=5,column=0)
    lbl6=Label(notif,text=msg[6]).grid(row=6,column=0)
    lbl7=Label(notif,text=msg[7]).grid(row=7,column=0)
    lbl8=Label(notif,text=msg[8]).grid(row=8,column=0)
    lbl9=Label(notif,text=msg[9]).grid(row=9,column=0)
    lbl10=Label(notif,text=msg[10]).grid(row=10,column=0)
    lbl11=Label(notif,text=msg[11]).grid(row=11,column=0)
    lbl12=Label(notif,text=msg[12]).grid(row=12,column=0)
    lbl13=Label(notif,text=msg[13]).grid(row=13,column=0)
    lbl14=Label(notif,text=msg[14]).grid(row=14,column=0)
    lbl15=Label(notif,text=msg[15]).grid(row=15,column=0)
    lbl16=Label(notif,text=msg[16]).grid(row=16,column=0)
    lbl17=Label(notif,text=msg[17]).grid(row=17,column=0)
    lbl18=Label(notif,text=msg[18]).grid(row=18,column=0)
    lbl19=Label(notif,text=msg[19]).grid(row=19,column=0)
    lbl20=Label(notif,text=msg[20]).grid(row=20,column=0)
    lbl21=Label(notif,text=msg[21]).grid(row=21,column=0)
    lbl22=Label(notif,text=msg[22]).grid(row=22,column=0)
    lbl23=Label(notif,text=msg[23]).grid(row=23,column=0)
    lbl24=Label(notif,text=msg[24]).grid(row=24,column=0)
    lbl25=Label(notif,text=msg[25]).grid(row=2,column=1)
    lbl26=Label(notif,text=msg[26]).grid(row=3,column=1)
    lbl27=Label(notif,text=msg[27]).grid(row=4,column=1)
    lbl28=Label(notif,text=msg[28]).grid(row=5,column=1)
    lbl29=Label(notif,text=msg[29]).grid(row=6,column=1)
    lbl30=Label(notif,text=msg[30]).grid(row=7,column=1)
    lbl31=Label(notif,text=msg[31]).grid(row=8,column=1)
    lbl32=Label(notif,text=msg[32]).grid(row=9,column=1)
    lbl33=Label(notif,text=msg[33]).grid(row=10,column=1)
    lbl34=Label(notif,text=msg[34]).grid(row=11,column=1)
    lbl35=Label(notif,text=msg[35]).grid(row=12,column=1)
    lbl36=Label(notif,text=msg[36]).grid(row=13,column=1)
    lbl37=Label(notif,text=msg[37]).grid(row=14,column=1)
    lbl38=Label(notif,text=msg[38]).grid(row=15,column=1)
    lbl39=Label(notif,text=msg[39]).grid(row=16,column=1)
    lbl40=Label(notif,text=msg[40]).grid(row=17,column=1)
    lbl41=Label(notif,text=msg[41]).grid(row=18,column=1)
    lbl42=Label(notif,text=msg[42]).grid(row=19,column=1)
    lbl43=Label(notif,text=msg[43]).grid(row=20,column=1)
    lbl44=Label(notif,text=msg[44]).grid(row=21,column=1)
    lbl45=Label(notif,text=msg[45]).grid(row=22,column=1)
    lbl46=Label(notif,text=msg[46]).grid(row=23,column=1)
    lbl47=Label(notif,text=msg[47]).grid(row=24,column=1)
    lbl48=Label(notif,text=msg[48]).grid(row=25,column=1)
    lbl49=Label(notif,text=msg[49]).grid(row=1,column=1)
    notif.grid(row=0,column=4,rowspan=50)



root=Tk()
#root.geometry("1080x720")
root.title("Camera Monitoring System")
input=Frame(root, width=100, height=100, bd=10)
heading=Label(input,text="DVR :",fg="white",bg="black", font = 'Verdana 14 bold').grid(row=0,column=0,columnspan=5,sticky=W+E,pady=10)

dvrlabel=Label(input,text="IP Address ").grid(row=1,column=0,sticky=W)
dvr=Entry(input)
dvr.insert(0,"192.168.1.3")
dvr.grid(row=2,column=0,padx=15,pady=5)

divLabel=Label(input,text="No. of Channels").grid(row=1,column=1,sticky=W)
channel=Entry(input)
channel.insert(0,"4")
channel.grid(row=2,column=1,padx=15,pady=5)

userlabel=Label(input,text="User Name").grid(row=1,column=2,sticky=W)
user=Entry(input)
user.insert(0,"admin")
user.grid(row=2,column=2,padx=15,pady=5)

passlabel=Label(input,text="Password").grid(row=1,column=3,sticky=W)
password=Entry(input)
password.insert(0,"admin@123")
password.grid(row=2,column=3,padx=15,pady=5)

path='rtsp://'+str(user.get())+':'+str(password.get())+'@'+str(dvr.get())+'/Streaming/Channels/01'
vid=cv2.VideoCapture(path)
ch=int(channel.get())
height = int(vid.get(3)) 
width = int(vid.get(4)) 

btn=Button(input,text="Enter",fg="LightBlue",bg="black",font='Verdana 10',command=partial(number_of_channels,channel,user,password,dvr))
btn.grid(row=2,column=4,sticky=W+E,padx=5,pady=5)
input.grid(row=0,column=0,columnspan=3)


video=Frame(root)
vidLabel=Label(video,text="Video Feed Goes Here...").grid(row=0,column=0,columnspan=2)

video.grid(row=1,column=0)

root.mainloop()