# 본 프로그램이 수행되기 위해서는 control 가상환경에 gtts가 설치되어야 함
# conda에서 control을 활성화한 후
# (control) > pip install gtts playsound 

import speech_recognition as sr 
from gtts import gTTS 
import os 
import time 
import playsound 

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3' 
    tts.save(filename) 
    playsound.playsound(filename) 

speak("안녕하세요. 길동씨")