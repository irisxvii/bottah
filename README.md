# Bottah
Bottah helps you to send emails simply by using your voice. <br/>
You can dictate the recipient's name, email subject, and body of the message, <br/>
and the system will handle the rest. <br/>

## How it works?
1. It prompts you to speak the name of the recipient.
2. Next, it asks you for the subject of your email.
3. After that, you are asked to speak the message content.
4. The email is then automatically sent to the selected recipient through your Gmail account.

## Libraries used
- Speech Recognition (speech_recognition)
- Text-to-Speech (pyttsx3)
- SMTP (smtplib)

## Setup and Usage:
1. clone the repo
2. install the required dependencies:

   ```
   pip install -r requirements.txt
     ```
3. create an .env file and set your gmail password:

   ```
   email_pass=your_gmail_password
      ```
4. run the program
5. follow the voice prompts to send your email!
   

