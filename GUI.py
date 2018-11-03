'''
import cv2
from tkinter import *
import tkinter as tk
import PIL
from tkinter import filedialog
import tkinter.messagebox 
from PIL import Image,ImageTk
from win32api import GetSystemMetrics
from functools import partial        #partial function is used to call functions
import sys,string,os

import pyautogui
import time
import os
def createLog(info):
	with open("log.txt","a+") as f:
		f.write(info+"\n")

def register(path,channels,root):
	createLog(path+channels)
	print(path+channels)
	result=tkinter.messagebox.askyesno("DVR Registered", "Want to register another DVR?", icon='warning')
	if result==True:
		main()
	else:
		root.destroy()


def main():
	root=Tk()
	root.title("Camera Monitoring System")
	input=Frame(root, width=100, height=100, bd=10)
	heading=Label(input,text="DVR :",fg="white",bg="black", font = 'Verdana 14 bold').grid(row=0,column=0,columnspan=5,sticky=W+E,pady=10)

	dvrlabel=Label(input,text="IP Address ").grid(row=1,column=0,sticky=W)
	dvr=Entry(input)
	dvr.grid(row=2,column=0,padx=15,pady=5)

	divLabel=Label(input,text="No. of Channels").grid(row=1,column=1,sticky=W)
	channel=Entry(input)
	channel.grid(row=2,column=1,padx=15,pady=5)

	userlabel=Label(input,text="User Name").grid(row=1,column=2,sticky=W)
	user=Entry(input)
	user.grid(row=2,column=2,padx=15,pady=5)

	passlabel=Label(input,text="Password").grid(row=1,column=3,sticky=W)
	password=Entry(input)
	password.grid(row=2,column=3,padx=15,pady=5)


	channels=str(channel.get())
	path='rtsp://'+str(user.get())+':'+str(password.get())+'@'+str(dvr.get())+'/Streaming/Channels/'
	print(password)
	btn=Button(input,text="Enter",fg="LightBlue",bg="black",font='Verdana 10',command=partial(register,path,channels,root))
	btn.grid(row=2,column=4,sticky=W+E,padx=5,pady=5)
	input.grid(row=0,column=0,columnspan=3)

	root.mainloop()

class Input(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Camera Monitoring System")
		self.heading=tk.Label(self,text="DVR :",fg="white",bg="black", font = 'Verdana 14 bold').pack()#.grid(row=0,column=0,columnspan=5,sticky=W+E,pady=10)
		self.dvrlabel=tk.Label(self,text="IP Address ").pack()#.grid(row=1,column=0,sticky=W)
		self.dvr=Entry(self)
		self.dvr.pack()
		#self.dvr.grid(row=2,column=0,padx=15,pady=5)

		self.divLabel=tk.Label(self,text="No. of Channels").pack()#.grid(row=1,column=1,sticky=W)
		self.channel=tk.Entry(self).pack()
		#self.channel.grid(row=2,column=1,padx=15,pady=5)

		self.userlabel=tk.Label(self,text="User Name").pack()#.grid(row=1,column=2,sticky=W)
		self.user=tk.Entry(self).pack()
		#self.user.grid(row=2,column=2,padx=15,pady=5)

		self.passlabel=tk.Label(self,text="Password").pack()#.grid(row=1,column=3,sticky=W)
		self.password=tk.Entry(self)
		#self.password.grid(row=2,column=3,padx=15,pady=5)

		self.channels=str(self.channel.get())
		self.path='rtsp://'+str(self.user.get())+':'+str(self.password.get())+'@'+str(self.dvr.get())+'/Streaming/Channels/'
		
		self.btn=tk.Button(self,text="Enter",fg="LightBlue",bg="black",font='Verdana 10',command=self.register()).pack()
		#self.btn.grid(row=2,column=4,sticky=W+E,padx=5,pady=5)


	def register(self):
		self.info=str(self.path)+str(self.channels)
		print(self.user.get())
		



app=Input()
app.mainloop()
print(app.info)
'''


'''
			make a page layout where you can switch between 3 screens 
			PAGE 1 for registering all the DVRs in the DVR.txt
			PAGE 2 	for running all the applications and displaying notifications and sending mail
			page 3 as a settings page
'''

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

def sum():
	return "345"

class testLayout(GridLayout):
	def show(self,input):
		if input:
			self.display.text=input
			print(input)
			err="nimbus"
			self.disp.text=sum()



class testApp(App):
 
    def build(self):
        return testLayout()


tApp=testApp()
tApp.run()