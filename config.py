import openai
import speech_recognition as sr
import pyttsx3
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("AziaIA escuchando...")
        audio = r.listen(source)
    return r.recognize_google(audio, language="es-MX")

def responder(texto):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": texto}]
    )
    return response['choices'][0]['message']['content']

def hablar(respuesta):
    engine = pyttsx3.init()
    engine.say(respuesta)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        try:
            pregunta = escuchar()
            respuesta = responder(pregunta)
            print("AziaIA:", respuesta)
            hablar(respuesta)
        except Exception as e:
            print("Error:", e)

