import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime
import cv2


def email(info,iterate=1):
	print("email",type(info))
	#print(info)
	message=str(info)
	'''
	for i in range(iterate):
		message=message+info[i]
	'''
	fromaddr="sujayrpi@gmail.com"
	toaddr="piyush@omnipresenttech.com"

	msg=MIMEMultipart()
	msg['From']=fromaddr
	msg['To']=toaddr
	msg['Subject']= 'Alert'
	msg.attach(MIMEText(message,'plain'))

	send=smtplib.SMTP('smtp.gmail.com',587)
	send.starttls()
	send.login(fromaddr,"sujay2908")

	text=msg.as_string()
	send.sendmail(fromaddr,toaddr,text)
	send.quit()

def saveImage(firstFrame,lastFrame,dvrIP,cam):
	times=str(datetime.datetime.now()
	cv2.imwrite("TamperedImages\\first "+times+".png",firstFrame)	
	cv2.imwrite("TamperedImages\\last "+times+".png",lastFrame)	

	email("Camera no {} of DVR {} has been tampered. \n The images for tampering the said camera have been saved as \n 	first"+times+"\n AND \n last"+times).format(cam,dvrIP)


if __name__ == '__main__':
	if not os.path.isdir("TamperedImages"):
        os.makedirs(("TamperedImages"))
	#email("oh darling tell me \n do we get what we deserve, and way down we go go go go")

