import pyttsx3
import speech_recognition as sr

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("AziaIA escuchando...")
        audio = r.listen(source)
    return r.recognize_google(audio, language="es-MX")

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
