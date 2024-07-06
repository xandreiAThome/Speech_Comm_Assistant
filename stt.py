# pip install vosk
# pip install pyaudio
# download speech model in https://alphacephei.com/vosk/models, unzip and place on same folder

from vosk import Model, KaldiRecognizer
import pyaudio

def speech_to_text(): 
    model = Model("vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while True:
        data = stream.read(4096)
        

        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            if(text[14:-3] == ""):
                print("Nothing follows")
                break
            
            print(f"' {text[14:-3]} '")

speech_to_text()