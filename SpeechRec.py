import speech_recognition as sr
from pyaudio import PyAudio, paInt16
from gtts import gTTS
import os
import pyttsx3
import pygame
import difflib
import time
import sys
import openai
import random
import subprocess


def loading_animation():
    loading_symbols = ["|", "/", "-", "\\"]
    for symbol in loading_symbols:
        sys.stdout.write("\rListening... %s" % symbol)
        sys.stdout.flush()
        time.sleep(0.2)

greetings_list={
    "hello": "Hello, how are you?",
    "hi": "Hi, how are you?",
    "hey": "Hey, how are you?",
    "good morning": "Good morning, how are you?",
    "good afternoon": "Good afternoon, how are you?",
    "good evening": "Good evening, how are you?",
    "good night": "Good night, how are you?",
    "good day": "Good day, how are you?",
    "good": "Good, how are you?",
    "how are you": "I am fine, how are you?",
    "how are you doing": "I am fine, how are you?",
    "how are you doing today": "I am fine, how are you?",
    "how is your day been": "not bad, how is your day been?",
    "thank you" and "thanks": "You are welcome",
}

sadness_data = {
    "I am sad": "I'm sorry to hear that. Is there anything I can do to help you feel better?",
    "I am depressed": "Depression is a serious matter. Have you considered seeking help from a mental health professional?",
    "I am unhappy": "It's okay to feel sad sometimes. Is there anything specific that you would like to talk about?",
    "I am disappointed": "Disappointments are tough, but it's important to remember that things will get better. Is there anything I can do to help you feel better?",
    "I am feeling down": "It's understandable to feel down sometimes. Talking to someone or engaging in a favorite activity can often help lift one's spirits.",
    "I am feeling low": "If you're feeling low, it may be helpful to take some time for self-care and to do things that make you happy. Would you like to talk about what's causing you to feel this way?",
    "I am feeling blue": "Feeling blue is a normal part of the ups and downs of life. You don't have to go through this alone. Is there someone you would like to talk to or something you would like to do to help improve your mood?"
}

commands = {
    "play music": "music",
    "turn off the computer": "shutdown",
    "open browser": "browser",
    "update windows": "update",
}
# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Say something...")
    engine.runAndWait()
    print("Listening...")
    audio_text = r.listen(source)
    loading_animation()
    print()
    audio = r.recognize_google(audio_text)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

for keyword in audio.split():
    found = False
    for key in sadness_data:
        if keyword in key.split():
            engine.say(sadness_data[key])
            engine.runAndWait()
            found = True
            break
    
    if found:
        continue

    for key in greetings_list:
        if keyword in key.split():
            engine.say(greetings_list[key])
            engine.runAndWait()
            found = True
            break

    if found:
        continue

    for key in commands:
        if keyword in key.split():
            if commands[key] == "music":
                pygame.mixer.init()
                # play a random music from web  
                pygame.mixer.music.play()
                engine.say("Playing music")
                engine.runAndWait()
                found = True
                break
            elif commands[key] == "shutdown":
                engine.say("Shutting down the computer")
                engine.runAndWait()
                os.system("shutdown /s /t 1")
                found = True
                break
            elif commands[key] == "browser":
                engine.say("Opening browser")
                engine.runAndWait()
                os.system("start chrome")
                found = True
                break
            elif commands[key] == "update":
                engine.say("Updating windows")
                engine.runAndWait()
                # open check for updates window 
                os.system("start ms-settings:windowsupdate")
                found = True
                break
            
    if not found:
        engine.say("I don't understand, can you repeat that?")
        engine.runAndWait()












# ---------- connecting through API to OpenAI ChatGPT ------------

# if you would like to use ChatGPT, please uncomment the following codes:

# # openAI api key
# openai.api_key = "YOUR API KEY"
# # open ai api
# model_engine = "text-davinci-002"

# prompt is the input text that you want to generate the response from

# prompt = audio
# completions = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# message = completions.choices[0].text
# engine.say(message)
# engine.runAndWait()

# ------------------------ Codes end here  -------------------------