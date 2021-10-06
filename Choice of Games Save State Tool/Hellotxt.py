from time import sleep
import sys, subprocess


#runs the TTS engin in another termainal to prevent it from interupting the text scrole
subprocess.Popen(['TTS Lines\HelloTTS.py'], shell=True, creationflags=subprocess.SW_HIDE)

sleep(0.5)

#runs the GUI in another termainal to prevent it from interupting the TTS
subprocess.Popen(['HellotxtGUI.py'], shell=True)
