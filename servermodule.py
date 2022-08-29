import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import os
import math
import random
import smtplib
from twilio.rest import Client
from validate_email import validate_email
from datetime import date
from datetime import datetime, timedelta
import string
import datetime
from anvil.pdf import PDFRenderer

mobileotp=0
emailotp=0
today=datetime.datetime.now() 
@anvil.server.callable      
def sendmail(mail):
  digits="0123456789"
  OTP=""
  for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
  otp = OTP + " is your OTP for ACS"
  msg= otp
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("anonymouscomplaintsystem@gmail.com", "iweyrsxxcgasyefq")
  emailid = mail
  s.sendmail('&&&&&&&&&&&',emailid,msg)
  addtotable(emailid,OTP)
  
  
  
@anvil.server.callable 
def sendotpsms(mobileno):
  otp = random.randint(1000,9999)
  account_sid = "AC8e259206b0d86d52ef5527698b2b853b"
  auth_token = "83c9e118107a918d5d37103aefb0b88e"
  client = Client(account_sid,auth_token)
  msg = client.messages.create(to = mobileno,from_ ="+19403735740",body = f"{otp} is your OTP for ACS")
  addtotable(mobileno,otp)

@anvil.server.callable 
def verifyotp(mailid,a):
  row=app_tables.otp_verification.get(EMAILID=mailid)
  otp=str(row['OTP'])
  row.delete()
  if(otp==a):
    return 1
  else:
    return 0

@anvil.server.callable  
def addtotable(mailid,a):
  app_tables.otp_verification.add_row(EMAILID=mailid,OTP=str(a),S=1)
  
@anvil.server.callable   
def addtoregistertable(reg_id,username,create_password,confirmpassword,email,mobile_no,location):
  app_tables.registertable.add_row(REGID=reg_id,CONPASSWORD=confirmpassword,CPASSWORD=create_password,MAILID=email,UNAME=username,S=1,Mobileno=mobile_no,loc=location
  )
  app_tables.reginfo.add_row(USERNAME=username,Password=confirmpassword,LOCATION=location,RID=reg_id)
  app_tables.currentlyregisteruser.add_row(RID=reg_id,S=1)
  
@anvil.server.callable   
def add_email_mobile(email,mobile):
  row=app_tables.currentlyregisteruser.get(S=1)
  r=row['RID']
  row1=app_tables.reginfo.get(RID=r)
  row1['MOBILENO']=mobile
  row1['EMAILID']=email
  row1['Date']=date.today()
  row.delete()
  
@anvil.server.callable 
def retrieveregtable():
  row=app_tables.registertable.get(S=1)
  us_name=row['UNAME']
  cre_pass=row['CPASSWORD']
  con_pass=row['CONPASSWORD']
  mail=row['MAILID']
  mobile=row['Mobileno']
  loc = row['loc']
  row.delete()
  return us_name,cre_pass,con_pass,mail,mobile,loc
  
@anvil.server.callable 
def r_regtable():
  row=app_tables.registertable.get(S=1)
  us_name=row['UNAME']
  cre_pass=row['CPASSWORD']
  con_pass=row['CONPASSWORD']
  mail=row['MAILID']
  mobile = row['Mobileno']
  loc = row['loc']
  return us_name,cre_pass,con_pass,mail,loc
video_room = ["P103630Ro0GzQnlC5Bg5","f4MEKvTXWSwbnG8gTrgM","Ifr7OZq45BFUkHyhSBaW","LRas440dglPrublMAQ7q","ROjaVFq3h5JCBXsc1TMq","aJAaf2F2GuyPSMwIHM9t","wLbZoPvjJdxNGXHPxp2T","wmLrdZk3pOdBfFRehDZs","bQC60Z78aJD5Pf2ja6oX","mRLafMaf17D3KE3D6Zrx"]  
voice_room = ["nucleus-jumphost-258","qqv69H9Iw4jA3TJIvQb2","WZUqswdabPus5blAmMQN","pP1FyCHMjgKMhNkOFzpy","nwtpwtGyIKzeqy5MTFmB","oa1vE7sXxSRQXVTOs2qo","13082002","WRL6Oa4kBHziy7Wsjq4O","KZ65p6zwJNqNnCdTDPZI","yK7depxhLhKvnSGB84nj"]
@anvil.server.callable 
def choose_video_room():
  index=random.randint(0,9)
  r_name = video_room[index]
  app_tables.room_code.add_row(RNAME=r_name,S=1)
@anvil.server.callable
def text_request(text):
  row = app_tables.currentlyloginuser.get(S=1)
  r=row['RID']
  row1=app_tables.reginfo.get(RID=r)
  loc=row1['LOCATION']
  user_emailid=row1['EMAILID']
  user_mobileno=row1['MOBILENO']
  row2=app_tables.police.get(Location=loc)
  mobileno=row2['Mobileno']
  email=row2['Emailid']
  row3=app_tables.room_code.get(S=1)
  roomname=row3['RNAME']
  row3.delete()
  s=random.randint(0,9)
  dat=today + datetime.timedelta(days=1)
  TIME = "07:00PM"
  app_tables.request_table.add_row(Request_text=text,Location=loc,ROOMCODE=roomname)
  link="https://QVC4AXL7TL5X5ASW.anvil.app/7PYSL6R4YVVFJ6EEKSBWBIHL"
  msg2 = "\nYou have requested for text consversation\nTIME:"+ TIME +"\nDate: "+dat.strftime('%d-%m-%Y')+ "\nTo connect click the below link and login and click connect with police and select join conversation and select text conversation then enter code below and start call then enter the x in username and enter code in channel,password then click enter channel\n"+"Link: "+link+"\ncode is "+roomname 
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("anonymouscomplaintsystem@gmail.com", "iweyrsxxcgasyefq")
  emailid = user_emailid
  s.sendmail('&&&&&&&&&&&',emailid,msg2)
  account_sid = "AC8e259206b0d86d52ef5527698b2b853b"
  auth_token = "83c9e118107a918d5d37103aefb0b88e"
  client = Client(account_sid,auth_token)
  msg = client.messages.create(to = user_mobileno,from_ ="+19403735740",body = f"\nYou have requested for text consversation\nTIME:{TIME}\nDate:{dat.strftime('%d-%m-%Y')} \nTo connect click the below link and login and click connect with police and select join conversation and select text conversation then enter code below and start call then enter the x in username and enter code in channel,password then click enter channel\n code is {roomname} \nLink: {link}")
  msg1 = "You have a text connect request from ACS app \n The request is " + text + "TIME:"+ TIME +"\nDate: "+dat.strftime('%d-%m-%Y')+ "\n if you want to connect click the below link and login and click connect with user and select join conversation and select text conversation then enter code below and start call then enter the y in username and enter code in channel,password then click enter channel\n"+"Link: "+link+"\ncode is "+roomname 
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("anonymouscomplaintsystem@gmail.com", "iweyrsxxcgasyefq")
  emailid = email
  s.sendmail('&&&&&&&&&&&',email,msg1)
  account_sid = "AC8e259206b0d86d52ef5527698b2b853b"
  auth_token = "83c9e118107a918d5d37103aefb0b88e"
  client = Client(account_sid,auth_token)
  msg = client.messages.create(to = mobileno,from_ ="+19403735740",body = f"\nYou have a text connect request from ACS app\n The request is {text}\nTime: {TIME}\n Date : {dat.strftime('%d-%m-%Y')}\n If you want to connect click the below link and login and click connect with user and select join conversation and select text conversation then enter code below and start call then enter the y in username and enter code in channel,password then click enter channel\n code is {roomname} \nLink: {link}")
  row.delete()
  
@anvil.server.callable
def send_voicerequest(text):
  row = app_tables.currentlyloginuser.get(S=1)
  r=row['RID']
  row1=app_tables.reginfo.get(RID=r)
  loc=row1['LOCATION']
  user_emailid=row1['EMAILID']
  user_mobileno=row1['MOBILENO']
  row2=app_tables.police.get(Location=loc)
  mobileno=row2['Mobileno']
  email=row2['Emailid']
  row3=app_tables.room_code.get(S=1)
  roomname=row3['RNAME']
  row3.delete()
  dat=today + datetime.timedelta(days=1)
  TIME = "07:00PM"
  app_tables.request_table.add_row(Request_text=text,Location=loc,ROOMCODE=roomname)
  link="https://QVC4AXL7TL5X5ASW.anvil.app/7PYSL6R4YVVFJ6EEKSBWBIHL"
  msg2 = "\nYou have requested for voice consversation\nTIME:"+ TIME +"\nDate: "+dat.strftime('%d-%m-%Y')+ "\nTo connect click the below link and login and click connect with police and select join conversation and select voice conversation then enter code below and start call then enter the code in password then click join room\n"+"Link: "+link+"code is "+roomname 
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("anonymouscomplaintsystem@gmail.com", "iweyrsxxcgasyefq")
  emailid = user_emailid
  s.sendmail('&&&&&&&&&&&',emailid,msg2)
  account_sid = "AC8e259206b0d86d52ef5527698b2b853b"
  auth_token = "83c9e118107a918d5d37103aefb0b88e"
  client = Client(account_sid,auth_token)
  msg = client.messages.create(to = user_mobileno,from_ ="+19403735740",body = f"\nYou have requested for voice consversation\nTIME:{TIME}\nDate:{dat.strftime('%d-%m-%Y')} \nTo connect click the below link and login and click connect with police and select join conversation and select voice conversation then enter code below and start call then enter the code in password then click join room\n code is {roomname} \nLink: {link}")
  msg1 = "You have a voice connect request from ACS app \n The request is " + text + "TIME:"+ TIME +"\nDate: "+dat.strftime('%d-%m-%Y')+ "\nIf you want to connect click the below link and login and click connect with user and select join conversation and select voice conversation then enter code below and start call then enter enter the code in password then click join room\n"+"Link: "+link+"\nCode is "+roomname
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("anonymouscomplaintsystem@gmail.com", "iweyrsxxcgasyefq")
  emailid = email
  s.sendmail('&&&&&&&&&&&',email,msg1)
  account_sid = "AC8e259206b0d86d52ef5527698b2b853b"
  auth_token = "83c9e118107a918d5d37103aefb0b88e"
  client = Client(account_sid,auth_token)
  msg = client.messages.create(to = mobileno,from_ ="+19403735740",body = f"\nYou have a voice connect request from ACS app\n The request is {text}\nTime: {TIME}\n Date : {dat.strftime('%d-%m-%Y')}\n If you want to connect click the below link and login and click connect with user and select join conversation and select voice conversation then enter code below and start call then enter the code in password then click join room\n code is {roomname} \nLink: {link}")
  row.delete()
  
@anvil.server.callable
def send_request(text):
  row = app_tables.currentlyloginuser.get(S=1)
  r=row['RID']
  row1=app_tables.reginfo.get(RID=r)
  loc=row1['LOCATION']
  user_emailid=row1['EMAILID']
  user_mobileno=row1['MOBILENO']
  row2=app_tables.police.get(Location=loc)
  mobileno=row2['Mobileno']
  email=row2['Emailid']
  row3=app_tables.room_code.get(S=1)
  roomname=row3['RNAME']
  row3.delete()
  dat=today + datetime.timedelta(days=1)
  TIME = "07:00PM"
  app_tables.request_table.add_row(Request_text=text,Location=loc,ROOMCODE=roomname)
  link="https://QVC4AXL7TL5X5ASW.anvil.app/7PYSL6R4YVVFJ6EEKSBWBIHL"
  msg2 = "\nYou have requested for video consversation\nTIME:"+ TIME +"\nDate: "+dat.strftime('%d-%m-%Y')+ "\nTo connect click the below link and login and click connect with police and select join conversation and select video conversation then enter code below and start call then enter the x in username and enter code in channel,password then click enter channel\n"+"Link: "+link+"code is "+roomname 
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("anonymouscomplaintsystem@gmail.com", "iweyrsxxcgasyefq")
  emailid = user_emailid
  s.sendmail('&&&&&&&&&&&',emailid,msg2)
  account_sid = "AC8e259206b0d86d52ef5527698b2b853b"
  auth_token = "83c9e118107a918d5d37103aefb0b88e"
  client = Client(account_sid,auth_token)
  msg = client.messages.create(to = user_mobileno,from_ ="+19403735740",body = f"\nYou have requested for video consversation\nTIME:{TIME}\nDate:{dat.strftime('%d-%m-%Y')} \nTo connect click the below link and login and click connect with police and select join conversation and select video conversation then enter code below and start call then enter the x in username and enter code in channel,password then click enter channel\n code is {roomname} \nLink: {link}")
  msg1 = "You have a video connect request from ACS app \n The request is " + text + "TIME:"+ TIME +"\nDate: "+dat.strftime('%d-%m-%Y')+ "\nIf you want to connect click the below link and login and click connect with user and select join conversation and select video conversation then enter code below and start call then enter the y in username and enter code in channel,password then click enter channel\n"+"Link: "+link+"\nCode is "+roomname
  s = smtplib.SMTP('smtp.gmail.com', 587)
  s.starttls()
  s.login("anonymouscomplaintsystem@gmail.com", "iweyrsxxcgasyefq")
  emailid = email
  s.sendmail('&&&&&&&&&&&',email,msg1)
  account_sid = "AC8e259206b0d86d52ef5527698b2b853b"
  auth_token = "83c9e118107a918d5d37103aefb0b88e"
  client = Client(account_sid,auth_token)
  msg = client.messages.create(to = mobileno,from_ ="+19403735740",body = f"\nYou have a  Video connect request from ACS app\n The request is {text}\nTime: {TIME}\n Date : {dat.strftime('%d-%m-%Y')}\n If you want to  connect click the below link and login and click connect with user and select join conversation and select video conversation then enter code below and start call then enter the y in username and enter code in channel,password then click enter channel\n code is {roomname} \nLink: {link}")
  row.delete()
  
@anvil.server.callable 
def choose_voice_room():
  index=random.randint(0,9)
  r_name = voice_room[index]
  app_tables.room_code.add_row(RNAME=r_name,S=1)

@anvil.server.callable 
def get_rname():
  row=app_tables.room_code.get(S=1)
  r_name = row['RNAME']
  row.delete()
  return r_name

@anvil.server.callable 
def add_unusual_info(c_type,file,desc,identif,loc):
  cid=random.randint(100000,9999999)
  app_tables.unusual.add_row(COMTYPE=c_type,FILE = file,DESCRIPTION=desc,IDENTIFICATION=identif,COM_ID=cid,Location=loc)
  
  
@anvil.server.callable 
def verifyuser(uname,password,mobieno):
  try:
    row=app_tables.reginfo.get(USERNAME=uname)
    if (row['Password']==password):
      if (row['MOBILENO']==mobieno):
        anvil.server.call('sendotpsms',mobieno)
        app_tables.currentlyloginuser.add_row(RID=row['RID'],S=1)
    else:
      return 1
  except:
    return 2
      
@anvil.server.callable
def validateemail(email):
  is_valid = validate_email(email)
  if is_valid==False:
    return 1
  else:
    return 0
  
@anvil.server.callable
def addcomplaintinfo(c_type,file,desc,identif,loc):
   cid=random.randint(100000,9999999)
   row=app_tables.currentlyloginuser.get(S=1)
   app_tables.complaintinfo.add_row(RID=row['RID'],COMTYPE=c_type,FILE = file,DESCRIPTION=desc,IDENTIFICATION=identif,COM_ID=cid,Location=loc,
                                    PDFFILE=PDFRenderer(page_size='A4',filename="COMPLAINT"+str(cid),margins={'top': 1.0, 'bottom': 1.0, 'left': 1.0, 'right': 1.0}).render_form('Form1.Form11'),FILESUBMITTEDDATE=str(today))
  
@anvil.server.callable
def policeloginverification(pid,password):
  row=app_tables.police.get(Policestationid=str(pid))
  p=row['Password']
  if(p==password):
    return 1
  else:
    return 0

@anvil.server.callable
def get_file(dat):
  pdfarr=[]
  row1=app_tables.currentlyloginpolice.get(S=1)
  pid=row1['Policestationid']
  row2=app_tables.police.get(Policestationid=pid)
  emailid=row2['Emailid']
  mobileno=row2['Mobileno']
  i=1
  for row in app_tables.complaintinfo.search(FILESUBMITTEDDATE=str(dat)):
    pdf1=row['PDFFILE']
    pdfarr.append(pdf1)
  anvil.email.send(
  from_name="ACS", 
  to=emailid, 
  subject="COMPLAINTS FROM ACS APP",
  text="COMPLAINT PDF OF "+str(dat)+" IS ATTACHED IN THIS EMAIL",
  attachments=pdfarr.copy()
  )
  
  
@anvil.server.callable
def addtocurrentlyloginpolice(pid):
  row=app_tables.currentlyloginpolice.add_row(Policestationid=pid,S=1)

