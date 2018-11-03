
		#### IMPORT ####
import multiprocessing
import cv2
import time
import os
import datetime
from mail import email
import subprocess
import numpy as np
        ### FUNCTIONS ###


def notify(cam,error_msg,dvrIP):
    error_msg=error_msg+"\n Camera no {} of DVR IP {} is not working".format(str(cam),dvrIP)
    return error_msg

def ch4dvr(frame,dvrIP):
    cams_on=np.array([101,201,301,401])
    (height,width)=frame.shape[:2]
    x1=int(width/2)
    y1=int(height/2)

    error_msg=""
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    frame1=cv2.calcHist([gray[0:y1,0:x1]],[0],None,[256],[0,256])
    frame2=cv2.calcHist([gray[0:y1,x1:width]],[0],None ,[256],[0,256])
    frame3=cv2.calcHist([gray[y1:height,0:x1]],[0],None,[256],[0,256])
    frame4=cv2.calcHist([gray[y1:height,x1:width]],[0],None,[256],[0,256])

    if frame4[0]>24000:
        error_msg=notify(4,error_msg,dvrIP)
        cams_on=np.delete(cams_on,3)  # (array,index)
    if frame3[0]>24000:
        error_msg=notify(3,error_msg,dvrIP)
        cams_on=np.delete(cams_on,2)
    if frame2[0]>24000:
        error_msg=notify(2,error_msg,dvrIP)
        cams_on=np.delete(cams_on,1)
    if frame1[0]>24000:
        error_msg=notify(1,error_msg,dvrIP)
        cams_on=np.delete(cams_on,0)

    #print("[ERROR]",error_msg)
    email(str(datetime.datetime.now())+error_msg)
    return cams_on

def ch8dvr(frame,dvrIP):
    cams_on=np.array([101,201,301,401,501,601,701,801])
    (height,width)=frame.shape[:2]   
    x1=int(width/3)
    x2=int(width*(2/3))
    y1=int(height/3)
    y2=int(height*(2/3))

    error_msg=""
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
        pass
    if frame8[0]>24000:
        error_msg=notify(8,error_msg,dvrIP)
        cams_on=np.delete(cams_on,7)
    if frame7[0]>24000:
        error_msg=notify(7,error_msg,dvrIP)
        cams_on=np.delete(cams_on,6)
    if frame6[0]>24000:
        error_msg=notify(6,error_msg,dvrIP)
        cams_on=np.delete(cams_on,5)
    if frame5[0]>24000:
        error_msg=notify(5,error_msg,dvrIP)
        cams_on=np.delete(cams_on,4)
    if frame4[0]>24000:
        error_msg=notify(4,error_msg,dvrIP)
        cams_on=np.delete(cams_on,3)
    if frame3[0]>24000:
        error_msg=notify(3,error_msg,dvrIP)
        cams_on=np.delete(cams_on,2)
    if frame2[0]>24000:
        error_msg=notify(2,error_msg,dvrIP)
        cams_on=np.delete(cams_on,1)
    if frame1[0]>24000:
        error_msg=notify(1,error_msg,dvrIP)
        cams_on=np.delete(cams_on,0)

    email(str(datetime.datetime.now())+error_msg)
    return cams_on

def checkDVR(lines):
    ret_val=""
    path=lines[:-1]
    dvrIP=path[-32:-20]
    path=path+"01"
    '''
    path='rtsp://admin:admin@123@192.168.0.78/Streaming/Channels/01'
    '''
    channel=int(lines[-1])
    print("path",path)
    vid=cv2.VideoCapture(path)
    startTime=time.time()
    while True:
        O_O,frame=vid.read()
        if not O_O and time.time()-startTime>30: #increse the time(seconds) and remove that break
            #print("DVR of IP {} not working".format(path[-34:-22]))
            file=open("log.txt",'a+')
            file.write(str(os.getpid())+"\n"+str(datetime.datetime.now())+" DVR of IP {} not working".format(dvrIP)+"\n")
            file.close()
            email(str(datetime.datetime.now())+" DVR of IP {} not working".format(dvrIP)+"\n")
            break
        elif channel==4:
            cams_on=ch4dvr(frame,dvrIP)
            for i in range(cams_on.shape[0]):
                print(str(path[:-2])+str(cams_on[i]))
            break
        elif O_O and channel==8:
            cams_on=ch8dvr(frame,dvrIP)
            break
        else:
            print("NOTHING")
            break       #important for breaking the loop
    vid.release()
    #return ret_val
    

if __name__=="__main__":

    file=open("DVR.txt","r+")
    lines=file.readlines()
    no_ofDVR=len(lines)
    deadpool=multiprocessing.Pool(processes=no_ofDVR)
    deadpool.map(checkDVR,iterable=lines)
    '''
    checkDVR(lines)
    '''
    print("DONE")