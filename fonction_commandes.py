# =========================================================
# crée le 21/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# coder les fonction permettant d'exécuter les commandes
# =========================================================

# bibliothèue importé
import webbrowser as wb
import pyautogui as pa
import time
import winreg
from pathlib import Path
import os
import subprocess
import pyttsx3

# ouverture page web
def open_web(nom_site=None):
    wb.open(nom_site)
  
# permet d'actionner des toches simultanément     
def act_key(touches=None):
    pa.hotkey(touches)

# recherche net
def search(sentences):
    wb.open("https://www.google.com")
    time.sleep(1)
    pa.write(sentences)
    pa.press('enter')

# lance une appli    
def start(words):
    desktop_appli_list = {}
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
    desktop_path = Path(winreg.QueryValueEx(key, "Desktop")[0])
    for items in desktop_path.iterdir():
        desktop_appli_list [os.path.basename(items).split(".")[0].lower()] = str(items)
    winreg.CloseKey(key)
    if words in desktop_appli_list:
        subprocess.Popen(desktop_appli_list[words], shell=True) 
    else:
        pyttsx3.init()
        pyttsx3.speak("L'application n'est pas installé")                                                   
        