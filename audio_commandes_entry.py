# =========================================================
# crée le 21/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# lire le fluw audio et en ressortir les mots-clé 
# d'activation des commandes et les exécuter
# =========================================================


# bibliothèque importé
import speech_recognition as sr 
import asyncio
import commandes_dic

# création d'instance de class
recognizer = sr.Recognizer()

# fonction d'entré des données audio
def audio_entry(entry=sr.Microphone(), languages='fr-FR', timeout=0.08, phrase_time_limit=3.5):
    with entry as mic:
        while 1:
            try:
                audio = recognizer.listen(mic, 
                              timeout=timeout, 
                              phrase_time_limit=phrase_time_limit
                              )   
                commandes = recognizer.recognize_google(audio_data=audio, language=languages)
            except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
                pass

audio_entry()
# recherche de commande