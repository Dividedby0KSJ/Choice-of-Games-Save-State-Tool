import pyttsx3

# initialize Text-to-speech engine
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)

TTSEngine.say("Back to game menu")
TTSEngine.runAndWait()