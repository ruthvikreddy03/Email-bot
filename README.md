# Voice-Controlled Email Sender

This is a Python-based project that allows users to send emails using voice commands. The application utilizes the `speech_recognition` and `pyttsx3` libraries for voice interaction and the `smtplib` library to send emails through Gmail.

## Features
- Send emails by providing voice input for the receiver, subject, and message.
- Uses the `speech_recognition` library to convert voice to text.
- Uses `pyttsx3` to provide voice feedback to the user.
- Supports sending emails via Gmail.

## Requirements
- Python 3.x
- `speech_recognition`, `pyttsx3`, and `smtplib` libraries

### Install the required libraries:
```bash
pip install SpeechRecognition pyttsx3
```

### How to Set Up
Clone the repository:
```
git clone https://github.com/yourusername/voice-email-sender.git
```
### Navigate to the project directory:

```bash
cd voice-email-sender
```

Make sure to enable "Less Secure Apps" in your Gmail account to allow the script to send emails on your behalf. You can enable this here.

Replace the placeholder values in the script with your email and password:

```python
server.login('Sender_Email', 'Sender_Email_password')
```
