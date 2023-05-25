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

recognizer = sr.Recognizer()

is_running = True


async def audio_entry(entry=sr.Microphone(), languages='fr-FR', timeout=0.08, phrase_time_limit=3.5):
    global mic, is_running
    with entry as mic:
        while is_running:
            try:
                audio = recognizer.listen(mic, 
                              timeout=timeout, 
                              phrase_time_limit=phrase_time_limit
                              )   
                commandes = recognizer.recognize_google(audio_data=audio, language=languages)     
            except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
                pass

asyncio.run(audio_entry())