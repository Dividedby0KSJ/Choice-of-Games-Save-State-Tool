import pyttsx3

# initialize Text-to-speech engine
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)

TTSEngine.say("The program has not been run before, please give admin permission to install the python modules")
TTSEngine.runAndWait()