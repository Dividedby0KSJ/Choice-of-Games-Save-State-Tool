import pyttsx3

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 200)
TTS.setProperty('volume',1)

TTS.say(
    "I need the path to store your save files!"
    "This information will be saved in the Variables folder!"
    "To change this, you must delete the 'RootDir.txt' File!"
)
TTS.runAndWait()