import pyttsx3

# initialize Text-to-speech engine
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)

TTSEngine.say("Wellcom to Divided's Choice of Games Save state tool!")
TTSEngine.runAndWait()