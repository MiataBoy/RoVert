import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')
engine.setProperty('volume', 1.0)


def speak(text) -> None:
    engine.say(text)
    engine.runAndWait()


def takecommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio, language='en-in')
            typeinput = input("Insert a command. If you wish to know what i am capable of; ask me what i can do.")
            print(f"user said:{user_input}\n")

            if typeinput:
                return typeinput

        except Exception as e:
            speak("Pardon me, please say that again")
            print("Caught exception when listening: ", e)
            return None
        return user_input


def wishme():
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
