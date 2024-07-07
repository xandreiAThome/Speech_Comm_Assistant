# downloads
# pip install pyttsx4

import pyttsx3

def text_to_speech():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for i in voices:
        print(i)
    engine.setProperty('voice', voices[0].id)
        # 
    engine.say("Hello, good morning")
    engine.runAndWait()

text_to_speech()