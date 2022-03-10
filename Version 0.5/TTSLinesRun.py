
import pyttsx3

TTS = pyttsx3.init()
TTS.setProperty('rate', 200)
TTS.setProperty('volume',0.4)

TTS.setProperty('rate', 300)
TTS.say("If you want to reset your saved RootDir, you can delete the 'RootDir.txt File'")
TTS.runAndWait()

TTS.setProperty('rate', 200)
TTS.say("Now I need the name of the game or what you want the code to call the game.")
TTS.say(" Warning! You can not use the following reserved characters!")
TTS.say("If you do it will error the code and not work.")
TTS.runAndWait()
