import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki
import pyautogui
import json
import smtplib
import requests
import openai
import comtypes.client
import pywhatkit as kit
import logging
import sample
sample.play_song(r"E:\downloads\[iSongs.info] 04 - Romeo Juliet.mp3")
logging.basicConfig(level=logging.ERROR)
r = sr.Recognizer()
x=pyttsx3.init()

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiODk3ZDkyMjMtYjcwNS00YmNmLWI2YzYtODFhYmNmZWViOGE5IiwidHlwZSI6ImFwaV90b2tlbiJ9.r2DUDE4W2aBItzrgGoUSzYREh4yqTsQpLaGjDkAL10c"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Mouli"
}



def talktoai(query):
    payload["text"]=query
   # print(payload)
    response=requests.post(url,json=payload,headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    speak(result['openai']['generated_text'])
   


def speak(audio):
    x.say(audio)
    x.runAndWait()
# speak("Hi I am Mouli AI How can I help you")
def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    print(t)
    speak(t)
#time() 
def date():
    y=str(datetime.datetime.now().year)
    m=str(datetime.datetime.now().month)
    d=str(datetime.datetime.now().day)   
    speak(d)
    speak(m)
    speak(y)
    # print (y)
# date()
def wish():
    hour = datetime.datetime.now().hour
    if hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("HI I am Mouli AI")
    speak("How can I help you")
#wish()
def browse(ques):
    kit.search(ques)
def whatsapp(msg):
    kit.sendwhatmsg_instantly(t,msg)
def sendemail(to,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('moulitopella@gmail.com','netm dhaz gkyn emok')
    server.sendmail('moulitopella@gmail.com',to,msg)
    server.close()    
def inp():
    x1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        x1.pause_threshold=1
        x1.adjust_for_ambient_noise(source)
        audio=x1.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Can you repeat again")
            inp()
            return "None"
        return query
#inp()        
def screenshot():
    im1 = pyautogui.screenshot()
    im1.save("C:/Users/Lenovo/cyoa/image.png")
def youtube(elem):
    kit.playonyt(elem)        
if __name__ =="__main__":
    wish()
    #t=inp()
    #t="Hi"
    while True:
        query=inp().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("I'm summarizing the wikipedia search...")
            query = query.replace("wikipedia", "")
            result = wiki.summary(query, sentences=2)
            print(result)
            speak(result)
        elif "screenshot" in query:
            speak("I'm taking screenshot of the screen...")
            screenshot()
        elif "open youtube" in query:
            try:
                speak("What you want to browse ?")
                elem=inp()
                speak("Opening youtube...")
                youtube(elem)
            except Exception as e:
                print(e)
                speak("Failed to browse")    
        elif "open chrome" in query:
            try:
                speak("What you want to search ?")
                ques=inp()
                speak("Browsing")
                browse(ques)
            except Exception as e:
                print(e)
                speak("Failed to browse")     
        elif "open Whatsapp" in query:
            try:
                 speak("Input receipient as text")
                 t=input()
                 speak("Msg to send")
                 msg=inp()
                 whatsapp(t,msg)
            except Exception as e:
                print(e)
                speak("Failed to send") 
        elif "remember" in query:
            speak("What to be rememberd ?")
            data=inp()
            speak("Your input is"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "speakout data" in query:
            remember=open('data.txt','r')
            speak("The data I stored is"+remember.read())
            #print("The data I stored is"+)
        elif "send email" in query:
            try:
                speak("What you want to send")
                msg=inp()
                speak("Enter recipient email")
                to=input()
                sendemail(to,msg)
                speak("It's success")
            except Exception as e:
                print(e)
                speak("retry") 
        elif "play a song" in query:
            song_path=input("Enter the song path:")
            sample.play_song(song_path)  
        elif "pause the song" in query:
            sample.control("pause") 
        elif "unpause" in query:
            sample.control("pause")
        elif "unpause" in query:
            sample.cotrol("unpause")
        elif "play" in query:
            try:
                sample.play_song(song_path) 
            except:
                print("please say play a song") 
        elif "stop" in query:
            sample.control("stop")
        elif "shutdown my pc" in query:
            os.system("shutdown /s /t 1")
        elif "restart my pc" in query:
            os.system("shutdown /r /t 1")                                            
        elif "exit" in query:
            speak("Exiting")
            print("Meet you Later")
            exit()
        else:
            talktoai(query)    


