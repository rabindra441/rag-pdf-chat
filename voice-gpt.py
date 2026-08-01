import speech_recognition as sr
import io
import sounddevice as sd
import soundfile as sf
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def speak(text):
    response = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="onyx",
        input=text,
        instructions="Speak like a calm, " \
        "intelligent AI assistant named Jarvis."
    )
    audio_bytes = io.BytesIO(response.content)
    data, samplerate = sf.read(audio_bytes)
    sd.play(data, samplerate)
    sd.wait()

def listen(duration=5, samplerate=16000):
    print("Listening....")
    audio_np = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    audio_bytes = io.BytesIO()
    sf.write(audio_bytes, audio_np, samplerate, format="WAV")
    audio_bytes.seek(0)

    r = sr.Recognizer()
    with sr.AudioFile(audio_bytes) as source:
        audio = r.record(source)
    return r.recognize_google(audio)

def ask_ai(text):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=text
    )
    return response.output_text

while True:
    text = listen()
    if text is None:
        continue

    print(f"You said: {text}")
    reply = ask_ai(text)
    print(f"Jarvice: {reply}")
    speak(reply)