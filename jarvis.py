import os
import random
from datetime import datetime
#from unittest import result
import webbrowser
#import content as content
import cv2
import pyttsx3
import speech_recognition as sr
import wikipedia
from requests import get
import pywhatkit as kit
import smtplib
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone () as source:
        print("listening......")
        r.pause_threshold =1
        audio = r.listen(source,timeout=25,phrase_time_limit=5)

    try:
        print("Recognizing...")
        queary=r.recognize_google(audio,language='en-in')
        print(f"user said:{queary}")
    except Exception as e :
        print("say that again please...")
        return "none"
    return queary
def wish():
    hour =int(datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak ("i am your assistent jarvis, sir please tell me how can i help you.")
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('nahidcebd@gmail.com','123456/n/789')
    server.sendmail('nahidcebd@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wish()
    while True:
    #if 1:
    #while True:

        queary = takecommand().lower()
        if "open screenshot photo please"in queary:
            speak("ok, sir im  opening screenshot photo!")
            npath ="C:\\Users\\88017\\OneDrive\\Pictures\\Screenshots"
            os.startfile(npath)
        elif "how are you jarvis" in queary:
            speak("i am fine, sir")
        elif"open command prompt"in queary:
            speak("ok,sir")
            os.system("start cmd")
            speak("do you have any other work")
        elif"open notepad"in queary:
            npath="C:\\Windows\\notepade"
            os.startfile(npath)
        elif"open camera"in queary:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k == 27:
                    break
                cap.release()
                cv2.destroyAllWindows()
        elif"open music"in queary:
            speak("ok, sir")
            music_dir = "C:\\Users\\88017\\Downloads\\New folder"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif "ip address" in queary:
            ip=get('https://api.ipify.org')
            speak(f"your IP address is {ip}")

        elif"wikipedia" in queary:
            speak("searching wikipedia....")
            queary=queary.replace("wikipedia", "")
            result=wikipedia.summary(queary,sentences=2)
            speak("according to Wikipedia")
            speak("result")
            print("result")

        elif"open youtube"in queary:
            webbrowser.open("www.youtube.com")
        elif "open facebook" in queary:
            webbrowser.open("www.facebook.com")
            speak("this is your facebook account,sir")
        elif "open w3schools" in queary:
            webbrowser.open("www.w3schools.com")
        elif "open stack overflow" in queary:
            webbrowser.open("www.stackoverflow.com")
        elif "open google" in queary:
            speak("sir,what should i search on google?")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        elif"send message"in queary:
            kit.sendwhatmsg("+8801798874485","this is nahid",8,8.5)
        elif"play songs on youtube" in queary:
            kit.playonyt("see you again")
            speak("do you have any other work,sir")
        elif"email to shameem" in queary:
            try:
                speak("what should i say?")
                content=takecommand().lower()
                to="rezashamim039@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to shameen")

            except Exception as e:
                print("e")
                speak("sorry sir,i am not able to send email")

        elif"no thanks"in queary:
            speak("thanks for using me sir,have a good day.")
        elif"you can sleep now" in queary:
            speak("thanks ,sir")
            sys.exit()
        elif"close youtube" in queary:
            speak("ok sir,closing youtube.")
            os.system("taskkill /f /im youtube.exe")
        elif"take a screenshot" in queary:
            speak("sir,please tall me the name of the screenshot file")
            name=takecommand().lower()
            speak("please sir hold the screen for few minite,i am taking screenshot")



        #speak("sir, do you have any othert work?")
