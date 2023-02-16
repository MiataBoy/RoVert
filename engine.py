import pyttsx3
import datetime
from information.public_data import NAME
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')
engine.setProperty('volume', 1.0)


def speak(text: str) -> None:
    engine.say(text)
    engine.runAndWait()


def takecommand() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio, language='en-us')
            print(f"user said:{user_input}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            print("Caught exception when listening: ", e)
        return user_input



def wishme() -> None:
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning, user.")
        print("Good morning, user.")

    elif 12 <= hour < 18:
        speak("Good afternoon, user.")
        print("Good afternoon, user.")
    else:
        speak("Good evening, user.")
        print("Good evening, user.")
