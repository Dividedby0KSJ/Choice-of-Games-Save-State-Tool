import pyttsx3

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 190)
TTS.setProperty('volume',1)

TTS.say(
    "I need your steamID3 without the brackets OR the 'U Colen 1 colen'?"
    "Use steamid.io to get your steamID3!"
)
TTS.runAndWait()