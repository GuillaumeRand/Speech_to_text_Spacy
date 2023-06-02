# Import packages
from numbers import Number
import speech_recognition as sr
import time 
from langdetect import detect


def recording():
    # initialize the recognizer
    r = sr.Recognizer()

    # Record voice trough microphone
    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Enregistrement...")
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
        print("Stop...")
    
        # convert speech to text
        try :
            print('Convertion de l\'audio en texte...')
            text = r.recognize_google(audio_data, language="fr-FR")

            # Save the record only if it's in French
            lang =detect(text)
            if lang == "fr":
                filename ="./vocal_{0}.txt".format(time.time())
                # Write the recorded sentences into file
                f = open(filename, "w")
                f.write(text)
                print(f"Traitement terminé : {filename}")
            else :
                print(f"L'enregistrement n'est pas français (reconnu: {lang})")
            
            print(text)
        except sr.UnknownValueError:
            print("L'enregistrement n'a pas reconnu de parole")

        return text