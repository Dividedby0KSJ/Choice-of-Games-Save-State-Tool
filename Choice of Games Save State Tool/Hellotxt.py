from time import sleep
import os, subprocess

with open(".\Wait.txt", "w") as Waittxt:
# Waittxt = open(".\Wait.txt", "w")
    Waittxt.writelines("Wait")
    Waittxt.close

#runs the TTS engin in another termainal to prevent it from interupting the text scrole
subprocess.Popen(['TTS Lines\HelloTTS.py'], shell=True, creationflags=subprocess.SW_HIDE)

sleep(0.5)

#runs the GUI in another termainal to prevent it from interupting the TTS
subprocess.Popen(['HellotxtGUI.py'], shell=True)

sleep(7)

os.remove("Wait.txt")