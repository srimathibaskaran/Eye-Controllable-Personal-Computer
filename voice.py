import smtplib
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import subprocess
from email.message import EmailMessage
import webbrowser
MASTER = "srimathi"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#speak function to pronounce the given string
def speak(text):
    engine.say(text)
    engine.runAndWait()

#the hello function
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning "+ MASTER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon "+ MASTER)
    else:
        speak("Good Evening "+ MASTER)


def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        audio  = r.listen(source)
    try :
        print("recognizing...")
        query = r.recognize_google(audio,language='en-IN')
        print(f"user said :{query}\n")

    except Exception as e:
        print("say that again ")
        query = "None"
    return query


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('coder25052003@gmail.com', 'yarehypfzixyuhgl')
    email = EmailMessage()
    email['From'] = 'coder25052003@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
email_list = {
                    'dude': 'COOL_DUDE_EMAIL',
                    'Srimathi'or'srimathi': 'srimathibaskaran25@gmail.com',
                    'yohasree': 'yohasree003@gmail.com',
                    'priyanka': 'priyanka.s@gmail.com',
                    
                }

speak("welcome to EC PC")
wishme()
speak(f"{MASTER} What do you want me to do for you : ")

def assistant(query):
    if 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current Time is {time}")

    elif "wikipedia" in query :
        query = query.replace('wikipedia','')
        speak("Searching Wikipedia ...")
        results = wikipedia.summary(query,sentences=2)
        speak(results)
        speak("Done Sir, Anything Else !")

     

    elif "google" in query :
        speak("Opening google ")
        url = "https://google.com"

        webbrowser.open(url)
        speak("Opened , Anything Else Sir")
    
    elif "enable eye control" in query :
        speak("Let's go")
        subprocess.Popen(["python", "mains.py"])
        speak("Done Sir, Anything Else !")
        
    elif "enable keyboard" in query :
        speak("Let's go")
        subprocess.Popen(["python", "vkeyboard.py"])
        speak("Done Sir, Anything Else !")

    elif "disable keyboard" in query :
        speak("Let's go")
        subprocess.Popen(["taskkill", "/f", "/im", "python.exe"])
        speak("Eye control disabled. Anything else, Sir?")

 
    elif "disable eye control" in query:
        speak("Disabling eye control...")
        subprocess.Popen(["taskkill", "/f", "/im", "python.exe"])
        speak("Eye control disabled. Anything else, Sir?")
    elif "send mail"in query:
        

        
        def get_email_info():
                                
                
                speak('To Whom you want to send email')
                name = takecmd()
                receiver = email_list[name]
                if receiver==None:
                    get_email_info()
                elif receiver!=email_list[name]:
                    get_email_info()
                    
                print(receiver)
                speak('What is the subject of your email?')
                subject = takecmd()
                speak('Tell me the text in your email')
                message = takecmd()
                send_email(receiver, subject, message)
                speak('Hey. Your email is sent')
                speak('Do you want to send more email?')
                send_more =takecmd()
                if 'yes' in send_more:
                    get_email_info()
                elif 'no':
                    return 0


        get_email_info()


    elif "bye" in query :
        speak(f"My pleasure to help you, {MASTER}. See you later")
        return 0
        
    else:
        print("I am not able to do this !")

while True:
    if assistant(takecmd().lower())==0:
        break

