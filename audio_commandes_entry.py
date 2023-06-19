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
        audio = recognizer.listen(mic, phrase_time_limit=5)
    # reconaissance des bouts de phrases
    commandes = recognizer.recognize_google(audio_data=audio, language='fr-FR')
    # découpage de la liste de mot
    list_words = commandes.lower().split()
    # recherche de commande a partir de la liste précedente    
    for i in list_words:      
        try: 
            choose_key = list_words[list_words.index(i)+1]
            if choose_key in keywords_choose:
                if choose_key in dic_commandes_touches:
                    order = dic_commandes_touches[choose_key]
                elif choose_key in dic_commandes_lien:
                    order = dic_commandes_lien[choose_key]
                else:
                    order = list_words[choose_key: -1]    
                        
            else:
                order = choose_key  
            print(order, i)    
            dic_commandes_type[i](order)  
        except (IndexError):
            pass           
