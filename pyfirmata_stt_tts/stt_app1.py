""" 이 프로그램을 수행하기 위해서는 하기의 package(depedancy)를 설치해야 함
    (control) vsc_workspace_foldr > pip install SpeechRecognition, pyaudio
"""                                 

import speech_recognition as sr  # speech -> text -> stt 
import webbrowser     # 이 패키지는 default 로 설치됨

#sr.Microphone(device_index=1)
r=sr.Recognizer()

r.energy_threshold=5000 #

with sr.Microphone() as source:
    print("아무말이나 하세요")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said: {}".format(text))
        url = "https://www.google.com/search?q=" 
        search_url = url+text
        webbrowser.open(search_url)
    except:
        print("Can't open url")