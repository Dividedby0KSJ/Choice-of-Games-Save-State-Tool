import pyttsx3

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 190)
TTS.setProperty('volume',1)

TTS.say(
    "I need the name of the game?"
    "You cannot use the following reserved characters!"
    "Check the exampil at the bottom."
)
TTS.runAndWait()