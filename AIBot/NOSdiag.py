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
#intro = "Hello I am Care Bear, the medical assistant. What are the symptoms you have been experiencing?"
# Converts introduction text to speech and save it as an audio file 
#text_to_speech(intro, 'intro.wav')

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

#searches for symptom mentions in user_words
def find_matching_word(input_string, word_list):
    words = []
    # Itereates over each word in the list
    for word in word_list:
        # Checks if the word is present in the input string
        if word in input_string:
            words.append(word)
    if words == []:
        return None
    else:
        return words

#list of symptoms that is matched for
symp_list = ['back pain','bladder discomfort','breathlessness','burning micturition','chest pain','chills','constipation','continuous sneezing','cough','cramps','fatigue','headache','high fever','indigestion','itching','joint pain','mood swings','muscle wasting','muscle weakness','neck pain','pain during bowel movements','patches in throat','pus filled pimples','shivering','skin rash','stiff neck','stomach pain','sunken eyes','vomiting','weakness in limbs','weight gain','weight loss','yellowish skin','acidity','anxiety','blackheads','bladder discomfort','blister','breathlessness','bruising','chest pain','chills','cold hands and feets','cough','cramps','dehydration','dizziness','fatigue','foul smell of urine','headache','high fever','indigestion','joint pain','knee pain','lethargy','loss of appetite','mood swings','nausea','neck pain','nodal skin eruptions','pain during bowel movements','pain in anal region','patches in throat','pus filled pimples','restlessness','shivering','skin peeling','skin rash','stiff neck','stomach pain','sunken eyes','sweating','swelling joints','ulcers on tongue','vomiting','weakness in limbs','weakness of one body side','weight gain','weight loss','yellowish skin','altered sensorium','anxiety','blackheads','blister','bloody stool','blurred and distorted vision','breathlessness','bruising','burning micturition','chest pain','chills','cold hands and feets','continuous feel of urine','cough','dark urine','dehydration','diarrhoea','dischromic  patches','dizziness','extra marital contacts','fatigue','foul smell of urine','headache','high fever','hip joint pain','joint pain','knee pain','lethargy','loss of appetite','loss of balance','mood swings','movement stiffness','nausea','neck pain','nodal skin eruptions','obesity','pain in anal region','red sore around nose','restlessness','scurring','silver like dusting','skin peeling','spinning movements','stomach pain','sweating','swelling joints','swelling of stomach','ulcers on tongue','vomiting','watering from eyes','weakness of one body side','weight loss','yellowish skin','altered sensorium','bloody stool','blurred and distorted vision','breathlessness','burning micturition','chest pain','continuous feel of urine','cough','dark urine','diarrhoea','dischromic  patches','distention of abdomen','dizziness','excessive hunger','extra marital contacts','family history','fatigue','headache','high fever','hip joint pain','irregular sugar level','irritation in anus','lack of concentration','lethargy','loss of appetite','loss of balance','mood swings','movement stiffness','nausea','obesity','painful walking','passage of gases','red sore around nose','restlessness','scurring','silver like dusting','small dents in nails','spinning movements','spotting  urination','sweating','swelling joints','swelling of stomach','swollen legs','vomiting','watering from eyes','weight loss','yellow crust ooze','yellowing of eyes','yellowish skin','blurred and distorted vision','breathlessness','chest pain','cough','dark urine','diarrhoea','distention of abdomen','dizziness','excessive hunger','family history','fatigue','headache','high fever','history of alcohol consumption','inflammatory nails','internal itching','irregular sugar level','irritation in anus','lack of concentration','lethargy','loss of appetite','loss of balance','mucoid sputum','nausea','painful walking','passage of gases','small dents in nails','spotting  urination','stiff neck','sweating','swelling joints','swollen blood vessels','swollen legs','unsteadiness','yellow crust ooze','yellowing of eyes','yellowish skin','blurred and distorted vision','breathlessness','chest pain','constipation','dark urine','depression','diarrhoea','dizziness','family history','fast heart rate','fluid overload','headache','high fever','history of alcohol consumption','inflammatory nails','internal itching','loss of appetite','malaise','mucoid sputum','nausea','obesity','painful walking','prominent veins on calf','puffy face and eyes','stiff neck','sweating','swelled lymph nodes','swollen blood vessels','unsteadiness','yellowing of eyes','yellowish skin','blurred and distorted vision','breathlessness','constipation','dark urine','depression','diarrhoea','enlarged thyroid','excessive hunger','fast heart rate','fluid overload','headache','irritability','loss of appetite','malaise','mild fever','muscle pain','nausea','obesity','phlegm','prominent veins on calf','puffy face and eyes','sweating','swelled lymph nodes','yellow urine','yellowing of eyes','brittle nails','chest pain','diarrhoea','drying and tingling lips','enlarged thyroid','excessive hunger','increased appetite','irritability','loss of appetite','malaise','mild fever','muscle pain','muscle weakness','nausea','phlegm','sweating','swelled lymph nodes','visual disturbances','yellow urine','yellowing of eyes','brittle nails','chest pain','diarrhoea','drying and tingling lips','fast heart rate','increased appetite','irritability','loss of appetite','malaise','mild fever','muscle weakness','pain behind the eyes','phlegm','polyuria','slurred speech','swelled lymph nodes','swollen extremeties','throat irritation','toxic look (typhos)','visual disturbances','yellowing of eyes','acute liver failure','back pain','belly pain','depression','fast heart rate','irritability','malaise','mild fever','muscle pain','pain behind the eyes','polyuria','receiving blood transfusion','red spots over body','redness of eyes','rusty sputum','slurred speech','swollen extremeties','throat irritation','toxic look (typhos)','yellowing of eyes','acute liver failure','back pain','belly pain','coma','depression','irritability','malaise','muscle pain','palpitations','receiving blood transfusion','receiving unsterile injections','red spots over body','redness of eyes','rusty sputum','sinus pressure','swelled lymph nodes','yellowing of eyes','coma','irritability','malaise','muscle pain','palpitations','receiving unsterile injections','runny nose','sinus pressure','stomach bleeding','swelled lymph nodes','congestion','malaise','muscle pain','phlegm','red spots over body','runny nose','stomach bleeding','congestion','phlegm','red spots over body','chest pain','loss of smell','loss of smell','muscle pain']
#looks for match
matching_symptoms = find_matching_word(user_words, symp_list)

#Saves matches to a file
with open('matched_symptoms.txt', 'a') as file:
    file.write(','.join(matching_symptoms))
    file.write("\n")


# Convert the response to speech and save it as an audio file
#text_to_speech(response, 'output.wav')

# Plays response audio
#play_audio_file('output.wav')    