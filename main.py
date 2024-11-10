import os
import smtplib
import speech_recognition as sr
import pyttsx3

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

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('gracegram06@gmail.com', email_pass)
    server.sendmail('gracegram06@gmail.com','iriskurien@gmail.com','testing second love')

def get_email_info():
    talk('who do u wanna send this to?')

get_email_info()
