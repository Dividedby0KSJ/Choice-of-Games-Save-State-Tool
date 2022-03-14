import pyttsx3

# VerNumber = str("0.1")

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 215)
TTS.setProperty('volume',1)

# # There is a bug that misses the first little bit of Welcome, so the 'a' Fixed it
# TTSEngine.say("Wellcom to Divided's Choice of Games Save state tool!")
# TTSEngine.runAndWait()

# TTSEngine.say("Version Number " + (VerNumber))
# TTSEngine.runAndWait()

TTS.say (
    "Wellcom to the New Game sript maker!"
    "I need a few things to make your game compatible with this tool!"
    "look at 'Your Variables & Help.txt' to get more info!"
)
TTS.runAndWait()