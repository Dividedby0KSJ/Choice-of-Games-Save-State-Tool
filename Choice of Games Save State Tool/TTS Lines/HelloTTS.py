import pyttsx3

VerNumber = str("0.5")

# initialize Text-to-speech engine
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)

TTSEngine.say("Wellcom to Divided's Choice of Games Save state tool!")
TTSEngine.runAndWait()
TTSEngine.say("Version Number " + (VerNumber))
TTSEngine.runAndWait()