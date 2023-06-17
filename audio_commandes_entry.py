# =========================================================
# crée le 21/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# avoir toutes les commandes permettant l'activation des
# commandes vocaux  
# =========================================================


# bibliothèque importé
import speech_recognition as sr 
import asyncio
from commandes_dic import *

# création d'instance de class
recognizer = sr.Recognizer()


def try_retry():
    with sr.Microphone() as mic:    
    # lecture du flux audio
        audio = recognizer.listen(mic, phrase_time_limit=3)
    # reconaissance des bouts de phrases
    commandes = recognizer.recognize_google(audio_data=audio, language='fr-FR')
    # découpage de la liste de mot
    list_words = commandes.split()
    # list de commandes à exécuter
    list_commandes = []
    # recherche de commande a partir de la liste précedente    
    for i in list_words:
        if i in keywords:
            list_commandes.append(i)     
    try:
        if len(list_commandes) == 2:    
            dic_commandes_type[list_commandes[0]](dic_commandes[list_commandes[1]])
        else:
            dic_commandes_type[list_commandes[0]]()    
    except (IndexError):
        pass           
