# MODULES INSTALLED
# To change ai assistant name replace name martin with your desired name
import time
import pyautogui
import pyttsx3
import datetime
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import random
from requests import get
import pyjokes
import PyPDF2


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #1 for female voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# WISH ME
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning user!")# replace user with your name

    elif hour>=12 and hour<18:
      speak("Good Afternoon user!")# replace user with your name

    else:
        speak("Good Evening user!")# replace user with your name


    speak("assistant activated")
    
    

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Understanding")
        query = r.recognize_google(audio, language='en-in')
        print(f"user sir Said: {query}\n")# replace user with your name

    except Exception as e:
        # print(e)    
        print("Pardon. Say that again")
        speak(" Pardon. Say that again")
        return "None"
    return query
# SEND EMAIL TO
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'you email password')
    server.sendmail('email to whom send the message', to, content)
    server.close()
# NEWS
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=408978ae28254145a421f03a2cc1c902'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):

        speak(f"today's{day[i]} news is: {head[i]}")
# WIKIPEDIA
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
# OPEN YOUTUBE
        elif 'open youtube' in query:
            speak('okay sir, opening youtube!')
            webbrowser.open("https://www.youtube.com")
# OPEN GOOGLE
        elif 'open google' in query:
            speak('okay sir, opening google!')
            webbrowser.open("https://www.google.com")
# OPEN GITHUB
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("okay sir, opening github")
# OPEN INSTAGRAM
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("okay sir, opening instagram")
# SEARCH SOMETHING ON GOOGLE
        elif 'search on google' in query:
            speak("What would you like to search on google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
#WISH ME BY NAME
        elif 'wish me' in query:
            speak("Hello user")# replace user with your name
# PLAY MUSIC FROM DIR
        elif 'play music' in query:
            speak('Playing Music!')
            music_dir = 'D:\\user' # replace user with your name
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
# WHATS THE TIME
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")
# OPEN COMMAND PROMPT
        elif 'open command prompt' in query or 'open CMD' in query:
            speak('Okay sir opening command prompt')
            os.system('start cmd')
# SEND EMAIL
        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "email id" # replace email id with your email id
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
               print(e)
               speak("Sorry,I am not able to send this email at the moment")
# PLAY MUSIC FROM YOUTUBE
        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)
# SIMPLE TALKS
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information user Created me ! I give Lot of Thanks to Him " # replace user with your name
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Martin an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello martin" in query:
            hel = "Hello Sir "
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! martin"  
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")
#IP ADDRESS
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
# JOKE
        elif "Tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
# SET ALARM
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'D:\\user' # replace user with your name
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
# SHUTDOWN
        elif "shut down" in query:
            os.system("shutdown /s /t 5")
# RESTART
        elif "restart" in query:
            os.system("shutdown /r /t 5")
# SLEEP
        elif "sleep" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
# NEWS
        elif "news" in query:
            speak("Please wait Sir,fetching the latest news")
            news()
# FIND LOCATION
        elif "where i am" in query or "where are we" in query:
            speak("wait sir let me check your current location")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f"Sir im not sure, but we are in {city} city {state} state of {country} country")
            except Exception as e:
                speak("Sorry Sir, Due to network issue i am not able to find where we are.")
                pass
# TAKE SCREENSHOT
        elif "take screenshot" in query:
            speak("Sir, Please tell me the name for the screenshot file")
            name = takeCommand().lower()
            speak("Taking Screenshot...!")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("ScreenShot Saved. You can see it ")

# TELL WEATHER OF CITY
        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("Tell you city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")
# PDF READER
        elif "read pdf" in query:
            pdf_reader()
            
        else:
            url = "http://api.brainshop.ai/get?bid=157984&key=3S0hhLXZ5GS2KYs4&uid=[uid]&msg=[{}]".format(query)
            response = requests.get(url).json()['cnt']
            print(response)
            speak(response)

while True:
    run_alpha()
