import pyttsx3

# initialize Text-to-speech engine
TTS = pyttsx3.init()
TTS.setProperty('rate', 150)

TTS.say(
    "The program cannot detect the os bit!"
    "Make sure that you are running this program in windows!"
    "If you are, and want to force the program to continue!"
    "Make a .txt file in the Variables directory with the architecturey you are running in!"
    "Example: Bit32.txt or Bit64.txt!"
    "Press enter to Exit"
)
TTS.runAndWait()