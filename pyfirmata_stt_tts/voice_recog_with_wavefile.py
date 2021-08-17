import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()

harvard = sr.AudioFile("F:\2021 2학기 강좌\control2\control2\pyfirmata_stt_tts\harvard.wav")
with harvard as source:
    audio = r.record(source)
    out_text = r.recognize_google(audio)

print(out_text)