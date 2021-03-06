import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import random as r
import os

from dotenv import load_dotenv
load_dotenv()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# 0 - Male, 1 - Female
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
    elif hour >=12 and hour <18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("Jarvis at your service. How may I help you?")

def takeCommand():
    # Takes microphone input from the user and returns string output

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
        print(e)
        print("Say that again please...")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, to, content)
    server.close()

if __name__ == "__main__":
    # speak("test")
    wishMe()
    while True:
        query = takeCommand().lower()
        
        # Logic to execute tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open github' in query:
            webbrowser.open('github.com')
        
        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            songs_list = list(songs)
            random_song = r.choice(songs_list)
            os.startfile(os.path.join(music_dir, random_song))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}\n")

        elif 'open code' in query:
            path = 'C:\\Users\\bests\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "bestspd6@gmail.com"
                sendEmail(to, content)
                speak("The email has been sent sir.")
            except Exception as e:
                print(e)
                speak("There seems to be a problem sir.")
