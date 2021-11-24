import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import json
import math
import operator
import wolframalpha
import pyautogui
import pyjokes
from translate import Translator
from PIL import Image,ImageFilter
import requests
import time
import cv2
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("hello i am your buddy how may i help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=18268887ed3e45cd8919422d785cd3c5'
    
    main_page = requests.get(main_url).json()  #print mainpage
    articles = main_page["articles"]
    head = []
    day = ["first","second","third"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #to print news
        speak(f"today's {day[i]} news is : {head[i]}")
        print(f"today's {day[i]} news is : {head[i]}")


if __name__ == "__main__":
    wishMe()
    while True:
     #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search' in query:
            speak('searching on wikipedia wait for a while ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
                          
        elif 'title' in query:
            title="Desktop Assistant"
            speak(f'name of your project is {title}')        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'instagram' in query:
            webbrowser.open("www.instagram.com/accounts/login")  

        elif 'facebook' in query:
            webbrowser.open("www.facebook.com")    

        elif 'twitter' in query:
            webbrowser.open("m.twitter.com/login")     

        elif 'play music' in query:
            #music_dir = ' //dir name '
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")
            print(strTime)

        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown") 
        elif 'volume mute' in query:
            pyautogui.press("volumemute")       

        elif 'game' in query:
            speak("your game will start soon. Be ready")
            import game   #importing game file

        elif 'joke' in query:
            joke=pyjokes.get_joke('en','neutral')
            speak(f'Todays joke is {joke}')
            print(joke)

        elif 'translate' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
              speak('What do you want to translate')
              audio=r.listen(source)
              voice_data=r.recognize_google(audio)
              t1=Translator(to_lang="es")
              t2=t1.translate(voice_data) 
              speak(f'In spanish {voice_data} means {t2}')
              print(f'In spanish: {voice_data} means- {t2}')  

        elif 'temperature' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
              speak('You wish to know temperature of which place')
              audio=r.listen(source)
              voice_data=r.recognize_google(audio)
              search=(f'temperature of {voice_data} is')
              url = f"https://www.google.com/search?q={search}"
              r=requests.get(url)
              data=BeautifulSoup(r.text,"html.parser")
              temp=data.find("div",class_="BNeawe").text
              speak(f'current {search} is {temp}')
              aa=(f'current {search} is {temp}')
              print(aa)

        elif 'calculate' in query or 'calculations' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:  
              speak('please can you tell me  What do you want to calculate')
              r.adjust_for_ambient_noise(source)
              audio=r.listen(source)
              vd=r.recognize_google(audio)
              print(vd)
            def get_operator_fn(op):
                return {
                    '+':operator.add, #plus
                    '-':operator.sub, #minus
                    'into':operator.mul, #into
                    'divided':operator.__truediv__, #divided
                    #'log':math.log, #log
                    
                }[op]  
            def eval_expr(op1,oper,op2):
                op1,op2=int(op1),int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("your result is")
            speak(eval_expr(*(vd.split())))  
            print("your result is")
            print(eval_expr(*(vd.split()))) 

        elif "news" in query:
            speak("please wait , fetching the latest news")
            news()

        elif 'take a screenshot' in query or 'screenshot' in query:  
                speak("friend, Please tell me the name for this screenshot file")
                name = takeCommand().lower()
                speak("friend hold this screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak(" friend your work is done , the screenshot is saved in your main folder")

        #  elif 'camera' in query: 
        #         cap = cv2.VideoCapture(0)
        #         while True:
        #             ret, img = cap.read()
        #             cv2.imshow('webcam',img)
        #             k = cv2.waitKey(50)
        #             if k==27:
        #              break;
        #         cap.release()
        #         cv2.destroyAllWindows()

        elif 'switch' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")   

        elif 'thanks' in query or 'thank you' in query:
            speak('welcome my friend i am here to help you whenever you need me')  
            print('welcome my friend i am here to help you whenever you need me')   
          
        else:
            speak("sorry say it again") 
            print("sorry say it again")       

           




              

       
            

       
        
          
         







