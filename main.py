import os
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except Exception as e:
        print("Error:", e) 

email_pass = os.getenv("email_pass")

if not email_pass:
    print("email_pass is not set.")

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('gracegram06@gmail.com', email_pass)
    email = EmailMessage()
    email['From'] = 'gracegram06@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'rebecca' : 'rebeccaebby5@gmail.com',
    'iris' : 'iriskurien@gmail.com',
    'leya' : 'leyariboy@gmail.com'
}

def get_email_info():
    talk('who do u wanna send this to?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('gimme the subject of your email')
    subject = get_info()
    talk('its time for the main text lessgoo. talk your heart out')
    message = get_info()
    send_email(receiver, subject, message)

get_email_info()
