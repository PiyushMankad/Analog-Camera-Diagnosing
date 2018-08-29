from tkinter import *
import tkinter as tkinter
import cv2
import time 
import sys


def do():
	print(dvr.get())

root=Tk()

root.title("Camera Monitoring System")
input=Frame(root, width=100, height=100, bd= 10)
heading=Label(input,text="DVR",fg = "Blue", font = 'Verdana 10').grid(row=0,column=0,columnspan=3)

dvrlabel=Label(input,text="IP Address ").grid(row=1,column=0,columnspan=3)
dvr=Entry(input)
dvr.insert(10,"192.168.1.3")
dvr.grid(row=2,column=0,columnspan=3,padx=5,pady=10)

divLabel=Label(input,text="No. of inputs ").grid(row=1,column=3)
div=Entry(input)
div.insert(0,"4")
div.grid(row=2,column=3,padx=5,pady=10)
input.grid(row=0,column=0,columnspan=3)

video=Frame(root)
vidLabel=Label(video,text="Video Feed Goes Here...").grid(row=0,column=0,columnspan=2)
video.grid(row=1,column=0)

notify=Frame(root)
lbl1=Label(notify,text=div.get()).grid(row=0,column=0)
lbl2=Label(notify,text=dvr.get()).grid(row=1,column=0)

notify.grid(row=0,column=4)

root.mainloop()