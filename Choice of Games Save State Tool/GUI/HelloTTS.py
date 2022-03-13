import pyttsx3
from time import sleep

VerNumber = str("0.1")

# initialize Text-to-speech engine
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)
TTSEngine.setProperty('volume',1)

sleep(0.4)

# There is a bug that misses the first little bit of Welcome, so the 'a' Fixed it
TTSEngine.say("a")
TTSEngine.say("Wellcom to Divided's Choice of Games Save state tool!")
TTSEngine.runAndWait()
TTSEngine.say("Version Number " + (VerNumber))
TTSEngine.runAndWait()
