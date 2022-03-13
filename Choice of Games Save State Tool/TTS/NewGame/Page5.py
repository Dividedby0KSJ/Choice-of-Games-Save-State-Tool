import pyttsx3

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 190)
TTS.setProperty('volume',1)

TTS.say(
    "I need the App ID of the game you want to save?"
    "Use steamdb.info to get the AppID of the game you want to save!"
)
TTS.runAndWait()