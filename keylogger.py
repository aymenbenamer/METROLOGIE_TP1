import os
import threading
from pynput.keyboard import Key, Listener
import time
from datetime import datetime

log = ""  
session_active = False  
start_time = None  
last_time = None  
idle_threshold = 30  
intervals = []  
path = os.path.join("/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt")

def get_timestamp():
    """ Retourne un timestamp au format YYYYMMDD HH:MM:SS """
    return datetime.now().strftime("%Y%m%d %H:%M:%S")

def calculate_typing_speed():
    """ Calcule la vitesse moyenne de frappe en mots par minute (WPM) """
    if intervals:
        avg_speed = (1 / (sum(intervals) / len(intervals))) * 60 / 5  # 5 caractères = 1 mot
        return round(avg_speed, 2)
    return 0

def processkeys(key):
    global log, last_time, session_active, start_time, intervals

    current_time = time.time()

    if last_time is not None:
        interval = current_time - last_time
        if interval > idle_threshold:  
            save_log()  # Sauvegarde la session précédente et met fin à l'enregistrement
            log = ""  
            intervals.clear()
            session_active = False  
        else:
            intervals.append(interval)  # 🔥 Ajoute l'intervalle entre les frappes

    last_time = current_time  

    try:
        if hasattr(key, 'char') and key.char is not None:
            if not session_active:
                log += get_timestamp() + "\t"  # Ajoute l'ID au début d'une nouvelle session
                start_time = current_time
                session_active = True

            log += key.char
        elif key == Key.space:
            log += " "
        elif key == Key.backspace and log:
            log = log[:-1]
        elif key == Key.enter:
            save_log()  # 📝 Sauvegarde et crée une nouvelle ligne avec un nouvel ID
            log = get_timestamp() + "\t"
            session_active = True
            intervals.clear()
    except AttributeError:
        pass

    print(f"Saisie actuelle : {log}")

def save_log():
    global log, path, session_active

    if log and session_active:
        typing_speed = calculate_typing_speed()
        log_entry = log + f"\t{typing_speed}\n"

        with open(path, "a", encoding="utf-8") as logfile:
            logfile.write(log_entry)

        print(f"💾 Log sauvegardé : {log_entry.strip()}")

        log = ""  
        session_active = False  
        intervals.clear()

def on_press(key):
    processkeys(key)

    if key == Key.esc:
        save_log()
        return False
    
def inactivity_check():
    """ Vérifie si l'utilisateur est inactif pendant plus de 15 secondes et sauvegarde le log. """
    global last_time

    while True:
        time.sleep(15)
        if last_time and (time.time() - last_time > idle_threshold):
            save_log()

# Thread pour surveiller l'inactivité
inactivity_thread = threading.Thread(target=inactivity_check, daemon=True)
inactivity_thread.start()

keyboard_listener = Listener(on_press=on_press)

with keyboard_listener:
    keyboard_listener.join()

