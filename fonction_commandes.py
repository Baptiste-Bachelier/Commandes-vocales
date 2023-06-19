# =========================================================
# crée le 21/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# coder les fonction permettant d'exécuter les commandes
# =========================================================

# bibliothèue importé
import webbrowser as wb
import pyautogui as pa

# ouverture page web
def open_web(nom_site=None):
    wb.open(nom_site)
    
def act_key(touches=None):
    pa.hotkey(touches)

def search(sentences):
    recherche = f"https://www.opera.com/search?q={sentences}"
    wb.open(recherche)       