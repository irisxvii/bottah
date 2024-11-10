import os
import smtplib
import speech_recognition as sr

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        info = listener.recognize_google(voice)
        print(info)

except Exception as e:
    print("Error:", e) 

email_pass = os.getenv("email_pass")

if not email_pass:
    print("email_pass is not set.")

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('gracegram06@gmail.com', email_pass)
    server.sendmail('gracegram06@gmail.com','iriskurien@gmail.com','testing second love')
