import pyttsx3

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 190)
TTS.setProperty('volume',1)

TTS.say(
    "Using The last SteamID3 That you inputed."
)
TTS.runAndWait()
