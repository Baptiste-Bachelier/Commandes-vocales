# =========================================================
# crée le 21/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# crée les fonctions pour les commandes
# =========================================================


# bibliothèque importé
from fonction_commandes import *
  
# dico des types de commandes
dic_commandes = {
    'YouTube':  'https://www.youtube.com' ,
    'Google':  'https://www.google.com'
}


# dico de commande 
dic_commandes_type = {
    'open': open_web,
    'quitter': close_web
    }

# list des clés de chaque dico
all_dic = [dic_commandes_type, dic_commandes]
# list mot clé
keywords = []
for i in all_dic:
    keywords.extend(i)
 