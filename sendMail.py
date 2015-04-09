import pandas as pd
import smtplib
import urllib2
import json
import sys
import MySQLdb
import warnings
import pandas as pd
import time
import requests
import os
######################################################################################################
MYSQL_HOST = "127.0.0.1"                                                                             #
MYSQL_PORT = 3306                                                                                    #
MYSQL_USER = "sureya"                                                                                #
MYSQL_PWD = "Emailss"                                                                                #
MYSQL_DB = "emails"                                                                                  #

#####################################################################################################

warnings.simplefilter(action = "ignore", category = FutureWarning)
warnings.simplefilter(action = "ignore", category = UserWarning)




def update_mails(to,subject,body,time):
	con = MySQLdb.connect (host = MYSQL_HOST, port = MYSQL_PORT, user = MYSQL_USER , passwd = MYSQL_PWD, db =MYSQL_DB )
	#cols = ["TO","Subject","Body"]
	
	time = str(time)
	#columns = cols
	frame = pd.DataFrame()

	frame.loc[time,"TO"] = to
	frame.loc[time,"Subject"] = subject
	frame.loc[time,"Body"] = body
	
	#frame = frame.astype(object).where(pd.notnull(frame), None)


	frame.to_sql(name="History",con=con,if_exists='append',flavor='mysql') 

	
def send_email():
	
	gmail_user = "catchsureya@gmail.com"
	
	print "Welcome Sureya, "
	f = open("pass_log.log","r")
	gmail_pwd = f.read()
	f.close()

	FROM = 'catchsureya@gmail.com'
	TO = [] #must be a list
	
	
	proceed = False

	temp = ""
	while ( temp != "*"):
		temp = raw_input("Enter the Mail Id, Press * to quit: ")
		if temp != '*' :
			TO.append(temp)
		print("Mail Id Received..")
	
	print "Mail id finalised."

	for ids in TO:
		if "@" not in ids or ".com" not in ids:
			print "The Mail id "+ids+" is not valid mail id."
			sys.exit()

	SUBJECT = raw_input("Enter the SUBJECT")
	print "\nEnter the Body of the mail.\n"
	text = ""
	stopword = "/done"
	while True:
	    line = raw_input()
	    if line.strip() == stopword:
	        break
	    text += "%s\n" % line# Prepare actual message
	print "You have typed:\n"+text

	message = 'Subject: %s\n\n%s' % (SUBJECT, text)
	try:
		#server = smtplib.SMTP(SERVER) 
		server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		#server.quit()
		server.close()
		print 'successfully sent the mail'
		time_sent = time.asctime( time.localtime(time.time()) )
		update_mails(TO,SUBJECT,text,time_sent)
		finish_flag = True

		return finish_flag
	except Exception as exp:
		print "failed to send mail bcz of "+str(exp)
		finish_flag = False
		return finish_flag


def connection():

    url = 'http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
        
    except requests.ConnectionError:
    	return False





if __name__ == "__main__":
	
	print "Checking the internet connectivity."

	net = connection()

	if net == True:
		print "Internet Works like a charm , Proceeding to Mail function."
		time.sleep(2)
		os.system('cls')
		send_email()

	elif net ==False:
		print "Internet Issues buddy."



