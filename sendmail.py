import smtplib     #simple mail transfer protocol
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

#defining data
email_user = "sankari0299@gmail.com"  #give your email id
email_sender = "ammalu02@gmail.com"   #give receiver id
subject = "Python testmail" #give your own subject
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_sender
msg['Subject'] = subject
body = "Hello! first mail using python script" # The \n separates the message
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login(email_user, "ammalu02") #give your pwd here 
#Send the mail
server.sendmail("sankari0299@gmail.com","ammalu02@gmail.com", text) 
server.quit()
