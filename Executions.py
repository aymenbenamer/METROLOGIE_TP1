import threading
import subprocess
import time

def run_keylogger():
    subprocess.run(["python3", "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/keylogger.py"])

def run_feelings_detection():
    while True:
        subprocess.run(["python3", "/Users/achrafbenamer/Desktop/METROLOGIE TP 1/FeelingsDetection.py"])
        time.sleep(15)

if __name__ == "__main__":
    keylogger_thread = threading.Thread(target=run_keylogger)
    feelings_detection_thread = threading.Thread(target=run_feelings_detection)

    keylogger_thread.start()
    feelings_detection_thread.start()

    keylogger_thread.join()
    feelings_detection_thread.join()