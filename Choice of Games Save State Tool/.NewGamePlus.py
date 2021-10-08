import pyttsx3, platform, glob, sys, subprocess, os
import PySimpleGUI as sg
from time import sleep


TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)

sg.theme('Black')   # Add a touch of color

#-------------------------------------------------------------------------------------------------------------------------


#this makes 2 py files, one of them to make the 
MasterOneLine = """\nimport pyttsx3\n\nTTSEngine = pyttsx3.init()\nTTSEngine.setProperty('rate', 190)\nTTSEngine.setProperty('volume',0.25)\nTTSEngine.say("Wellcom to the game sripts maker! I need to ask a few things to make your Cog game compatible with this tool!")\nTTSEngine.runAndWait()\n"""

with open(".\TTSLinesRun.py", "w") as TTSLinesRun:
    TTSLinesRun.writelines([MasterOneLine])
    TTSLinesRun.close

subprocess.Popen(['TTSLinesRun.py'], shell=True, creationflags=subprocess.SW_HIDE)

#--------------------------------------------------------------------------------------------------------------------------
NewGamePlusLayout1 = [
    [sg.Text('Wellcom to the game sripts maker! I am dev.')],
    [sg.Text('\nI need to ask a few things to make your Cog game compatible with this tool!')],
    [sg.Text("\nPlease look at 'Your Variables & Help.txt' to get more info!\n", text_color='dark gray')],
    [sg.Button(button_text="Next", key="Next",)]
]

# print("Wellcom to the game sripts maker! \nI am dev.")
# print("I need to ask a few things to make your Cog game compatable with this tool!")
# print("\nPlease look at 'Your Variables & Help.txt' to get more info!\n")

NewGamePlusWindow1 = sg.Window("Introduction", NewGamePlusLayout1, font=('',17), element_justification='Center')

while True:
    event, values = NewGamePlusWindow1.read(timeout=100)
    if event == sg.WIN_CLOSED:
        exit()
    if event == 'Next':
        break

NewGamePlusWindow1.close()

sleep(0.2)

os.remove("TTSLinesRun.py")

#-----------------------------------

if glob.glob("RootDir.txt"): #if file is alredy available
    print("\n\n\n\nUsing The last RootDir That you inputed. \nIf you want to reset it than del the 'RootDir.txt' File")
    #open file here
    RootDirFile = open(".\RootDir.txt", "r")
    RootDir = RootDirFile.readline()
    RootDirFile.close
    # ass

else:
    # print("\nFirst I'm Going to need the path you want to store your save files\n")
    # print("E.g: >>> C:/Users/YourUserName/Saved Games/CogSST <<<\n")
    # print("its caled in this code RootDir. So please type the path without '' {Quotation Marks}\n And with '/' insead of 'BackSlash' \n")
    # print("\nOh And this is semi-permanent!! \nSo if you want to change this than you must delete the 'RootDir.txt' File as well as re-make your game save/load files\n")
    # RootDir = input(("RootDir\n>"))
    # #assert

    #this makes 2 py files, one of them to make the 
    MasterOneLine = """\nimport pyttsx3\n\nTTSEngine = pyttsx3.init()\nTTSEngine.setProperty('rate', 200)\nTTSEngine.setProperty('volume',0.4)\nTTSEngine.say("First I'm Going to need the path you want to store your save files.")\nTTSEngine.say("..")\nTTSEngine.say("Oh And this is semi-permanent!! So if you want to change this than you must delete the 'RootDir.txt' File as well as re-make your game save/load files")\nTTSEngine.runAndWait()\n"""

    with open(".\TTSLinesRun.py", "w") as TTSLinesRun:
        TTSLinesRun.writelines([MasterOneLine])
        TTSLinesRun.close

    subprocess.Popen(['TTSLinesRun.py'], shell=True, creationflags=subprocess.SW_HIDE)


    NewGamePlusLayout2_0RootDir = [
        [sg.Text("First I'm Going to need the path you want to store your save files")],
        [sg.Text("E.g: >>> C:/Users/YourUserName/Saved Games/CogSST <<<")],
        [sg.Text("If you input the path manuly please type the path without '' {Quotation Marks}\n and with '/' insead of 'BackSlash' \nIts better if you just use the folder browser!", font=("", 20), text_color="Red")],
        [sg.Text("\nOh And this is semi-permanent!! \nSo if you want to change this than you must delete the 'RootDir.txt' File as well as re-make your game save/load files")],
        [sg.Text("Root Dir >", justification='Right') , sg.Input(focus=True, key='RootDir_Input'), sg.FolderBrowse('Folder'), sg.Button(button_text='Submit', button_color='Green')],
    ]

    NewGamePlusWindow1_2 = sg.Window("RootDir", NewGamePlusLayout2_0RootDir, font=('',14), element_justification='Center')

    while True:
        event, values = NewGamePlusWindow1_2.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Submit':
            RootDir_Value = values['RootDir_Input'] or 'ERROR'
            break
        
        
    NewGamePlusWindow1_2.close()

    os.remove("TTSLinesRun.py")

    RootDirFile = open(".\RootDir.txt", "x")
    RootDirFile.writelines(RootDir_Value)
    RootDirFile.close
    RootDirFile = open(".\RootDir.txt", "r")
    RootDir = RootDirFile.readline()
    RootDirFile.close

#this makes 2 py files, one of them to make the 
MasterOneLine = """\nimport pyttsx3\n\nTTS = pyttsx3.init()\nTTS.setProperty('rate', 200)\nTTS.setProperty('volume',0.4)\n\nTTS.setProperty('rate', 300)\nTTS.say("If you want to reset your saved RootDir, you can delete the 'RootDir.txt File'")\nTTS.runAndWait()\n\nTTS.setProperty('rate', 200)\nTTS.say("Now I need the name of the game or what you want the code to call the game.")\nTTS.say(" Warning! You can not use the following reserved characters!")\nTTS.say("If you do it will error the code and not work.")\nTTS.runAndWait()\n"""

with open(".\TTSLinesRun.py", "w") as TTSLinesRun:
    TTSLinesRun.writelines([MasterOneLine])
    TTSLinesRun.close

subprocess.Popen(['TTSLinesRun.py'], shell=True, creationflags=subprocess.SW_HIDE)

NewGamePlusLayout2_1GameName = [
    [sg.Text("If you want to reset your saved RootDir, you can delete the 'RootDir.txt File'", text_color='DarkGray')],
    [sg.Text('\nNow I need the name of the game or what you want the code to call the game.', font=('', 16))],
    [sg.Text("! YOU CANNOT USE !", text_color='Red', font=('impact', 20))],
    [sg.Text("The following reserved characters:\n < (less than) \n > (greater than) \n : (colon) \n '' (double quote) \n / (forward slash) \n \ (backslash) \n | (vertical bar or pipe) \n ? (question mark) \n * (asterisk) \n ", text_color='black', background_color='white')],
    [sg.Text("! IF YOU DO IT WILL ERROR THE CODE AND NOT WORK !\n", text_color='Red', font=('impact', 20))],
    [sg.Text("Original Name > 'Werewolves: Haven Rising'", justification='center')],
    [sg.Text("Name You Should Use > Werewolves Haven Rising", justification='center')],
    [sg.Text("Game Name >", justification='Right') , sg.Input(focus=True, key='Game_Name_Input'), sg.Button(button_text='Submit', button_color='Green')],
]

NewGamePlusWindow2 = sg.Window("Introduction", NewGamePlusLayout2_1GameName, font=('',14), element_justification='Center')

while True:
    event, values = NewGamePlusWindow2.read(timeout=100)
    if event == sg.WIN_CLOSED:
        exit()
    if event == 'Submit':
        Game_Name = values['Game_Name_Input'] or 'ERROR'
        break
    
NewGamePlusWindow2.close()

os.remove("TTSLinesRun.py")

# print("\n\n\n\nNow I need the name of the game or what you want the code to call the game.\n")
# print("!YOU CANNOT USE! The following reserved characters: < (less than) > (greater than) \n : (colon) [I cant show you it] (double quote) / (forward slash) \ (backslash) | (vertical bar or pipe) \n ? (question mark) * (asterisk) \n IF YOU DO IT WILL ERROR THE CODE AND NOT WORK\n")
# print("E.g: >>> Werewolves Haven Rising [O.G Name (Werewolves: Haven Rising)] <<<\n")
# Game_Name = input(("Game Name\n>"))

if glob.glob("SteamID3.txt"): #if file is alredy available
    print("\n\n\n\nUsing The last SteamID3 That you inputed. \nIf you want to reset it than del the 'SteamID3.txt' File")
    #open file here
    SteamID3File = open(".\SteamID3.txt", "r")
    steamID3 = SteamID3File.readline()
    SteamID3File.close


else:

    print("\n\n\n\nNow I need your steamID3 without the '[]' OR 'U:1:'\nUse steamid.io to get yous\n\nRemeber! DO NOT INCLUDE THE '[]' OR 'U:1:'")
    # steamID3 = input(("steamID3\n>"))
    SteamID3File = open(".\SteamID3.txt", "x")
    SteamID3File.writelines(input(("steamID3\n>")))
    SteamID3File.close
    SteamID3File = open(".\SteamID3.txt", "r")
    steamID3 = SteamID3File.readline()
    SteamID3File.close

print("\n\n\n\nOK this is (almost) the last one!\nI need the Appid of the game.\nGoto steamdb.info and serch your games name and copy paste the App ID here!")
Appid = input(("Appid\n>"))

# print("\n\n\n\nOK. OK. OK... THIS is the last one and it is the simplest one\nWhat is your windows os bit? it can only be 32 or 64 (or the code wont work)\n and you can only input 32 or 64\nIf you dont know, open 'System Information' and look under 'System type' if it says x64-based than you are 64.\n")
# OS_32_or_64 = input(("OS_32_or_64\n>"))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if glob.glob("Bit64.txt"): #if file is alredy available
    print("64bit")
    OS_32_or_64 = "64"

elif glob.glob("Bit32.txt"): #if file is alredy available
    print("32bit")
    OS_32_or_64 = "32"

else: # Finds out what OSbit it is

    OSbit = platform.machine().endswith('64')

    # print(OSbit)


#---------------------------------------------------------------- Bit Prosesing -------------------------------------------------------
 
    def Bit64():

        Bit1 = open(".\Bit64.txt", "x")
        Bit1.writelines("64Bit OS, the beast one!")
        Bit1.close

    def Bit32():

        Bit2 = open(".\Variables\Bit32.txt", "w")
        Bit2.writelines("32Bit OS or x86")
        Bit2.close


#----------------------------------------------------- Bit Detections ---------------------------------------------------------------

if OSbit == True:
    print("this is 64bit")
    Bit64()

elif OSbit == False:
    print("this is not 64bit")
    Bit32()

else:
    print("this is not 64bit or 32bit \n ERROR: Unknown OSbit")
    exit()


#----------------------------------------------------------------------------------------------------------------------------------

# The file to read from
BassCode_File = open(".\Bass Code V2.py", "r")

# The file in RAW str with lines, so its like a copy paste!
BassCode_Str = BassCode_File.readlines()

BassCode_File.close()


NewGame = open("CogSST-" + (Game_Name) + ".py", "w")

NewGame.writelines(BassCode_Str)

NewGame.close()


BassCode_Str[15] ="RootDir = r'" +(RootDir) +"'\n"

BassCode_Str[18] ="Game_Name = r'" +(Game_Name) +"'\n"

BassCode_Str[23] ="steamID3 = " +(steamID3) +"\n"

BassCode_Str[27] ="Appid = " +(Appid) +"\n"

BassCode_Str[30] ="OS_32_or_64 = " +(OS_32_or_64) +"\n"

NewGame = open("CogSST-" + (Game_Name) + ".py", "w")

new_file_contents = "".join(BassCode_Str)

NewGame.write(new_file_contents)
NewGame.close()