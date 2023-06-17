# =========================================================
# crée le 28/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# lire le fluw audio et en ressortir les mots-clé 
# d'activation des commandes et les exécuter
# =========================================================


# bibliothèque ou fichier importé
from audio_commandes_entry import *

   
# reconaissance et activation des commandes 

while 1:
    try:
        try_retry()  
    except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError, KeyError):
        pass