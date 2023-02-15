import ctypes

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
from information import sources, tokens

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')
engine.setProperty('volume', 1.0)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")

    elif 12 <= hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        typeinput = input("Please type in your command if you'd like to type...")
        if typeinput:
            userstatement = typeinput
        else:
            audio = recognizer.listen(source)

            try:
                userstatement = recognizer.recognize_google(audio, language='en-in')
                print(f"user said:{userstatement}\n")

            except Exception as e:
                speak("Pardon me, please say that again")
                print("Caught exception when listening: ", e)
                return "None"
        return userstatement


print("Loading your AI personal assistant RoVert")
speak("Loading your AI personal assistant RoVert")
wishme()

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takecommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant RoVert is shutting down,Good bye')
            print('your personal assistant RoVert is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            news = webbrowser.open_new_tab(sources.news)
            speak('Here are some headlines from AD,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", f"RoVertImg.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            speak('Searching for {}'.format(statement))
            webbrowser.open_new_tab("https://google.com/search?q=" + statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer computational and geographical questions. Please state your question.')
            question = takecommand()
            client = wolframalpha.Client(tokens.WOLFRAM_TOKEN)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am RoVert release 1 point O, your personal assistant. I am programmed to perform minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow as well as predict time, take a photo, '
                  'search wikipedia and predict the weather'
                  'In different cities, get top headline news from AD.nl and you can ask me computational or '
                  'geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by MiataBoy based on code by Mirthula")
            print("I was built by MiataBoy based on code by Mirthula")

        elif "weather" in statement:
            api_key = tokens.OPENWEATHER_TOKEN
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takecommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
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

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            time.sleep(10)
            subprocess.call(["shutdown", "/l"])

        elif "shut down" in statement or "power off" in statement or "turn off" in statement:
            speak("Alright. Shutting down your pc in 10 seconds. While Windows generally closes remaining programs itself, we recommend closing them yourself beforehand to prevent any loss of progress.")
            time.sleep(10)
            subprocess.call(["shutdown", "/s"])

        elif "lock" in statement:
            speak("Alright, locking your pc.")
            ctypes.windll.user32.LockWorkStation()

        elif "mitchel" in statement and "cute" in statement:
            speak("Yes, Mitchel is indeed cute.")

        else:
            speak(f"Sorry, i could not understand {statement}. I am currently only capable of performing basic tasks like opening youtube, wikipedia and google searches. I can also find the weather for you and perform geographical and computational questions.")

time.sleep(3)


