# now we will add subject and make sure to address is visible along with body of email using email packages

import smtplib #simple mail transfer protocol mime ---> Mulit puprose Internet mail extensionn protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#definiing data
From="nakkamanikanta1903@gmail.com" # give your email.id
to="kakkireninikhilesh26@gmail.com"# give reciver gmail.id
subject="tranniee in python"
msg=MIMEMultipart()
msg["From"]=From
msg["to"]=to
msg["subject"]=subject
body="hello! frist mail using python script" #the /n separate the message
msg.attach(MIMEText(body,"plain"))
text=msg.as_string()
#same usage of smtplib to start the process
server=smtplib.SMTP("smtp.gmail.com",578)
server.starttls()
#next ,log in to the server
server.login(From,"qvhq nxzy lopy oygn")
#give your app passcode here send the mail
server.sendmail(From,to,text)
print("Mail sent")
server.quit()
