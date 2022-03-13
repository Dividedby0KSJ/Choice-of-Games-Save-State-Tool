import PySimpleGUI as sg
import subprocess, base64, os, glob

#----------------------------------------------------- OS Dir Check -------------------------------------------------------

# System 32 Dir Check
Sys32 = os.getcwd()
if Sys32 == "C:\WINDOWS\system32":
    print ("!!! For some reason, the program has started in System32! !!! \nThe program can not run in this directory. please check the help file for how to fix")
    input("Press enter to exit...")
    exit()


# Check if If in the github directory or in the Release directory
if os.path.exists(r"./Choice of Games Save State Tool") :
    # Change the current working Directory    
    os.chdir(r"./Choice of Games Save State Tool")
# else:
#     print("Can't change the Current Working Directory\nOr Already in correct directory.")


#----------------------------------------------------- Wait TXT -------------------------------------------------------


# with open(".\Wait.txt", "w") as Waittxt:
# # Waittxt = open(".\Wait.txt", "w")
#     Waittxt.writelines("Wait")
#     Waittxt.close


#----------------------------------------------------- Logo -------------------------------------------------------

# Info gotten from:
# https://appdividend.com/2020/06/23/how-to-convert-image-to-base64-string-in-python/
# This converts the Logo to base64 for PyGUI
with open(".\GUI\DCogStt.png", "rb") as DCogStt_file:
    DCogStt_64 = base64.b64encode(DCogStt_file.read())
# DCogStt_64 = b'DCogStt_64_Raw'


#----------------------------------------------------- TTS -------------------------------------------------------


#this makes 2 py files, one of them to make the 
MasterOneLineHelloTTS = """\nimport pyttsx3\nfrom time import sleep\n\nVerNumber = str("0.1")\n\n# initialize Text-to-speech engine\nTTSEngine = pyttsx3.init()\nTTSEngine.setProperty('rate', 190)\nTTSEngine.setProperty('volume',1)\n\nsleep(0.4)\n\n# There is a bug that misses the first little bit of Welcome, so the 'a' Fixed it\nTTSEngine.say("a")\nTTSEngine.say("Wellcom to Divided's Choice of Games Save state tool!")\nTTSEngine.runAndWait()\nTTSEngine.say("Version Number " + (VerNumber))\nTTSEngine.runAndWait()\n"""

with open(".\GUI\HelloTTS.py", "w") as HelloTTS:
    HelloTTS.writelines([MasterOneLineHelloTTS])
    HelloTTS.close

subprocess.Popen(['.\GUI\HelloTTS.py'], shell=True, creationflags=subprocess.SW_HIDE)


#----------------------------------------------------- GUI -------------------------------------------------------


sg.theme('Black')   # Add a touch of color


# The text and image, to make it centred I have to pass it into another layout
HelloTxTlayoutC = [
    [sg.Text("Wellcom to Divided's", font=("arial", 30), text_color='Yellow')],
    [sg.Text("Choice of Games Save state tool!", font=("arial", 30), text_color='Yellow')],
    [sg.Text("Made by 'Kieren St James' (Divided By 0)", font=("arial", 20), text_color='lightgray')],
    [sg.Text("Revision #2 v.0.0.6", font=("arial", 20), text_color='red')],
    [sg.Text("You can click the logo to skip to the menue", font=("impact", 16), text_color='DarkGray')],
    [sg.Image(source=DCogStt_64, enable_events=True, key='Logo')]
]


# Centers the text
HelloTxTlayout = [
    [sg.Column(HelloTxTlayoutC, element_justification='center')]
]


# Create the Window
HelloTxTWindow = sg.Window("Wellcom To Divided's CogSST", HelloTxTlayout, size=(1150,730) ,auto_close=True, auto_close_duration=7)


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = HelloTxTWindow.read()
    if event == sg.WIN_CLOSED or event == 'Logo': # if user closes window or clicks cancel
        break


HelloTxTWindow.close()

# if glob.glob("Wait.txt"):
#     os.remove("Wait.txt")