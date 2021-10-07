import os, subprocess
from time import sleep

OneLine = """\nimport pyttsx3\n\nTTSEngine = pyttsx3.init()\nTTSEngine.setProperty('rate', 190)\nTTSEngine.say("Wellcom to the game sripts maker! I need to ask a few things to make your Cog game compatible with this tool!")\nTTSEngine.runAndWait()\n"""

with open(".\TTSLines.py", "w") as TTSLines:
    TTSLines.writelines([OneLine])
    TTSLines.close

subprocess.Popen(['TTSLines.py'], shell=True, creationflags=subprocess.SW_HIDE)

sleep(1)

os.remove("TTSLines.py")