import smtplib #simple mail transfer protocol
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls() #transport layer security

#Next,log in to the server
server.login("sankari0299@gmail.com","ammalu02")

#send the email
msg = "Hello!First mail using python script"
#the \n separates the message from the headers

#message from the headers
server.sendmail("sankari0299@gmail.com","ammalu02@gmail.com",msg)




