import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

gmail_user = "sankari0299@gmail.com" #enter your gmail username
gmail_pwd = "ammalu02" #enter your passwd
to = 'ammalu02@gmail.com' #enter to whom you want to send
subject = "Please find the attachment"
text = "I'm sharing the jpeg file" #body of mail
attach = 'signature.jpeg' #give your attachment name
msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(text))
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',
   'attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)
mailServer = smtplib.SMTP("smtp.gmail.com",587)
mailServer.starttls()
mailServer.login(gmail_user, gmail_pwd)
mailServer.sendmail(gmail_user, to, msg.as_string())
# Should be mailServer.quit(), but that crashes...
mailServer.close()

