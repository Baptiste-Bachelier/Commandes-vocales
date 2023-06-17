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
def open_web(url=None):
    wb.open(url)
    
def close_web():
    pa.hotkey("ctrl", "w")