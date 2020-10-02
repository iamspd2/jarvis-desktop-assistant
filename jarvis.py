import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# 0 - Male, 1 - Female
engine.setProperty('voice',voices[0].id)
# engine.say("Friday at service. How are you doing?")
# engine.runAndWait()

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

if __name__ == "__main__":
    # speak("test")
    wishMe()