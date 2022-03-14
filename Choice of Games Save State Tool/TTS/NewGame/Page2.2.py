import pyttsx3

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 210)
TTS.setProperty('volume',1)

TTS.say(
    "Using Last RootDir entered."
)
TTS.runAndWait()