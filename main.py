import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import os

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_info(timeout=5):
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source, timeout=timeout)  # add timeout here
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Please try again.")
        return get_info()
    except sr.WaitTimeoutError:  # handle timeout error
        talk("Timeout! Please try again.")
        return get_info()


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('band21cs016@rmkcet.ac.in', '7075899695')
    email = EmailMessage()
    email['From'] = 'band21cs016@rmkcet.ac.in'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'dude': 'digu21cs038@rmkcet.ac.in',
    'bts': 'apav21cs001@rmkcet.ac.in',
}


def get_email_info():
    clear_screen()
    talk('To Whom you want to send email')
    name = get_info()
    clear_screen()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    clear_screen()
    talk('Tell me the text in your email')
    message = get_info()
    clear_screen()
    send_email(receiver, subject, message)
    talk('Hey lazy ass. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    clear_screen()
    if 'yes' in send_more:
        get_email_info()


get_email_info()