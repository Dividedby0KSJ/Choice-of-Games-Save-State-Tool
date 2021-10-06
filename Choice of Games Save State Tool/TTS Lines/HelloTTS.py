import pyttsx3
from time import sleep

VerNumber = str("0.9")

# initialize Text-to-speech engine
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)

sleep(0.4)

# The is a bug that missis the first little bit of Welcome, so the 'a' Fixed it
TTSEngine.say("a")
TTSEngine.say("Wellcom to Divided's Choice of Games Save state tool!")
TTSEngine.runAndWait()
TTSEngine.say("Version Number " + (VerNumber))
TTSEngine.runAndWait()