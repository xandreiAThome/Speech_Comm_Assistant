# pip install piper-tts
# echo 'Welcome to the world of speech synthesis!' | piper \ --model en_US-lessac-medium \ --output_file welcome.wav
# python version 3.10.14

import os
import wave
from piper.voice import PiperVoice

# replace path with the path of the onnx file
model_path = "path"
voice = PiperVoice.load(model_path)
wav_file = wave.open('output.wav', 'w')
text = "This is an example of text-to-speech using Piper TTS."
audio = voice.synthesize(text,wav_file)