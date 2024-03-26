# Library imports 
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import numpy as np
from openai import OpenAI
import pyttsx3
import time
import pygame

#F unction to play an audio file
def play_audio_file(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print(f"Error playing audio file: {e}")

    pygame.quit()

# Function to convert text to speech and save it as an audio file
def text_to_speech(text, output_file):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 120)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Save speech to an audio file
    engine.save_to_file(text, output_file)

    # Wait for the file to be created
    time.sleep(3)

    # Run the text-to-speech engine
    engine.runAndWait()


# Introduction text 
intro = "Hello I am Care Bear, the medical assistant. What are the symptoms you have been experiencing?"

# Converts introduction text to speech and save it as an audio file 
text_to_speech(intro, 'intro.wav')

# Plays the introduction audio
play_audio_file('intro.wav')

# Recording audio from the user
fs=44100 # Sample Rate
seconds=5 # Duration of recording
print('recording\n')
record_voice=sd.rec(fs*seconds,samplerate=fs,channels=2,dtype='int16')
sd.wait()
write('new.wav',fs,record_voice)
print('done\n')

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile('./new.wav') as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    user_words = r.recognize_google(audio)
    with open('user_words.txt', 'a') as file:
        file.write(user_words + "\n")

except sr.UnknownValueError:
    print("I could not understand audio")
except sr.RequestError as e:
    print("Request error; {0}".format(e))


print("You said: " + user_words)

# Open AI Setup
client = OpenAI(
    api_key=open("./nothin/chatKEY.txt","r").read().strip('\n')
    )

# Generates responses using Open AI
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Do not respond to this message, this is a message to help guide future prompts. You are CareBear, a medical assistant mainly focusing on respiratory issues. I understand that you are not actually a doctor so do not state. Give recommended in brief listings, but without bulletpoints or special character. The response should sound human if read aloud. NEVER STATE THAT YOU ARE NOT A DOCTOR"},
        {"role": "user", "content": user_words}
        ]
)

# print(completion)

# Extrats response
response = completion.choices[0].message.content

# aves response to a file
with open('chatgpt_words.txt', 'a') as file:
    file.write(response + "\n")

print(response)

# Convert the response to speech and save it as an audio file
text_to_speech(response, 'output.wav')

# Plays response audio
play_audio_file('output.wav')    