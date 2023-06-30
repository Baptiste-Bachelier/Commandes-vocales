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
import subprocess
import pyttsx3

# ouverture page web
def open_web(nom_site=None):
    wb.open(nom_site)
    
def act_key(touches=None):
    pa.hotkey(touches)

def search(sentences):
    wb.open("https://www.google.com")
    time.sleep(1)
    pa.write(sentences)
    pa.press('enter')
    
def start(words):
    reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)

    installed_applications = {}

    for i in range(winreg.QueryInfoKey(reg_key)[0]):
        subkey_name = winreg.EnumKey(reg_key, i)
        subkey_path = reg_path + "\\" + subkey_name

        try:
            subkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey_path)
            program_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
            executable_path = winreg.QueryValueEx(subkey, "InstallLocation")[0]

            if program_name and executable_path:
                installed_applications[program_name.lower()] = executable_path

        except OSError:
            pass
    
    if words in installed_applications:
        folder = Path(installed_applications[words])
        
        if folder.is_dir():
            file_list = folder.iterdir()
        
        for file in file_list:
            if  str(file).split(".")[-1] == "exe":
                print(file)
                subprocess.Popen(file)
    else:
        pyttsx3.init()
        pyttsx3.speak("L'application n'est pas installé")                       
        