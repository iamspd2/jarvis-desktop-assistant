import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# 0 - Male, 1 - Female
engine.setProperty('voice',voices[1].id)
# engine.say("Friday at service. How are you doing?")
# engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("test")