import os
import smtplib

email_pass = os.getenv("email_pass")

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('gracegram06@gmail.com', email_pass)
server.sendmail('gracegram06@gmail.com','iriskurien@gmail.com','testing love')
