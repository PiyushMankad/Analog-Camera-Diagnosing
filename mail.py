import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def email(info,iterate=1):
	print(type(info))
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

if __name__ == '__main__':
	email("oh darling tell me \n we get what we deserve, and way down we go go go go")

