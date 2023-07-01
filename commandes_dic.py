# =========================================================
# crée le 21/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# crée les fonctions pour les commandes
# =========================================================


# bibliothèque importé
from fonction_commandes import *
  
# dico des types de commandes
dic_commandes_lien = {
    # lien 
    'youtube': 'https://www.youtube.com',
    'amazon': 'https://www.amazon.fr',
}
dic_commandes_touches = {
    # touches
    'fermer': "ctrl w".split(),
    'quitter': "alt F4".split(),
    'changer': "alt tab".split(),
    'sauvegarder': "ctrl s".split() 
}


# dico de commande 
dic_commandes_type = {
    'ouvre': open_web,
    'start': start,
    'commande': act_key,
    'cherche': search
    }

# list mot clé
keywords_type = []
for i in dic_commandes_type:
    keywords_type.extend(i)
    
keywords_choose = []
for i in zip(dic_commandes_lien, dic_commandes_touches):
    keywords_choose.extend(i) 