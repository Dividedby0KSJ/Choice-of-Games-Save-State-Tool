import PySimpleGUI as sg
from time import sleep
import os, subprocess, glob, platform
from runpy import run_path

sg.theme('Black')   # PySimpleGUI Theme

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


#----------------------------------------------------- Wait.txt Clean -------------------------------------------------------

if glob.glob("Wait.txt"):
    print("This shouldint be here!")
    os.remove("Wait.txt")

#----------------------------------------------------- Code --------------------------------------------------------------------------------------------------------------


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Page 1 [Introduction] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Checks to see if there is any saved Variables, if there is, than it skips the introduction.

if glob.glob(".\Variables\*"):
    print("This has been run before, skiping the tutorial")

else:
    #TTS For the GUI 
    subprocess.Popen([r".\TTS\NewGame\Page1.py"], shell=True, creationflags=subprocess.SW_HIDE)


    NewGameLayoutIntroduction = [
        [sg.Text('Wellcom to the New Game sript maker! I am Divided.')],
        [sg.Text('\nI need to ask a few things to make your Cog game compatible with this tool!')],
        [sg.Text("\nPlease look at 'Your Variables & Help.txt' to get more info!\n", text_color='dark gray')],
        [sg.Button(button_text="Next", key="Next",)]
    ]


    NewGameWindowIntroduction = sg.Window("Introduction", NewGameLayoutIntroduction, font=('',17), element_justification='Center')


    while True:
        event, values = NewGameWindowIntroduction.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Next':
            break


    NewGameWindowIntroduction.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Page 2 [RootDir] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Im thinking that the Rootdir may not be necessary and may remove later, however I would like the user to have control where thay want there files to go.

if glob.glob(".\Variables\RootDir.txt"): #if file is alredy available
    subprocess.Popen([r".\TTS\NewGame\Page2.2.py"], shell=True, creationflags=subprocess.SW_HIDE)
    print("\n\n\n\nUsing The last RootDir That you inputed. \nIf you want to reset it than del the 'RootDir.txt' File")
    #open file here
    RootDirFile = open(".\Variables\RootDir.txt", "r")
    RootDir = RootDirFile.readline()
    RootDirFile.close


else:

    subprocess.Popen([r".\TTS\NewGame\Page2.py"], shell=True, creationflags=subprocess.SW_HIDE)


    NewGameLayoutRootDir = [
        [sg.Text("First I'm Going to need the path you want to store your save files")],
        [sg.Text("E.g: >>> C:/Users/YourUserName/Saved Games/CogSST <<<")],
        [sg.Text("Its better if you just use the folder browser!\nIt's recommended to use the DCogSST folder in the programs folder", font=("", 20), text_color="Red")],
        [sg.Text("\nThis information will be saved in the Variables folder. \nSo if you want to change this than you must delete the 'RootDir.txt' File")],
        [sg.Text("Root Dir >", justification='Right') , sg.Input(focus=True, key='RootDir_Input', default_text="C:/Users/YourUserName/Saved Games/CogSST"), sg.FolderBrowse('Folder'), sg.Button(button_text='Submit', button_color='Green')],
    ]


    NewGameWindowRootDir = sg.Window("RootDir", NewGameLayoutRootDir, font=('',14), element_justification='Center')


    while True:
        event, values = NewGameWindowRootDir.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Submit':
            RootDir_Value = values['RootDir_Input'] or 'ERROR'
            break


    NewGameWindowRootDir.close()


    RootDirFile = open(".\Variables\RootDir.txt", "x")
    RootDirFile.writelines(RootDir_Value)
    RootDirFile.close
    RootDirFile = open(".\Variables\RootDir.txt", "r")
    RootDir = RootDirFile.readline()
    RootDirFile.close


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Page 3 [Game Name] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


subprocess.Popen([r".\TTS\NewGame\Page3.py"], shell=True, creationflags=subprocess.SW_HIDE)

NewGameLayoutGame_Name = [
    [sg.Text("If you want to reset your saved RootDir, you have to delete the 'RootDir.txt File'", text_color='DarkGray')],
    [sg.Text('\nNow I need the name of the game or what you want the code to call the game.', font=('', 16))],
    [sg.Text("!!  YOU CANNOT USE  !!\n!!  THE FOLLOWING RESERVED CHARACTERS  !!", text_color='Red', justification='center', font=('impact', 20))],
    [sg.Text(" < (less than) \n > (greater than) \n : (colon) \n '' (double quote) \n / (forward slash) \n \ (backslash) \n | (vertical bar or pipe) \n ? (question mark) \n * (asterisk)", text_color='black', background_color='white')],
    [sg.Text("!!  IF YOU DO IT WILL ERROR THE CODE AND NOT WORK  !!\n", text_color='Red', font=('impact', 20))],
    [sg.Text("Original Name > 'Werewolves: Haven Rising'", justification='center')],
    [sg.Text("Name You Should Use > Werewolves Haven Rising", justification='center')],
    [sg.Text("Game Name >", justification='Right') , sg.Input(focus=True, key='Game_Name_Input'), sg.Button(button_text='Submit', button_color='Green')],
]


NewGameWindowGame_Name = sg.Window("Game Name", NewGameLayoutGame_Name, font=('',14), element_justification='Center')


while True:
    event, values = NewGameWindowGame_Name.read(timeout=100)
    if event == sg.WIN_CLOSED:
        exit()
    if event == 'Submit':
        Game_Name = values['Game_Name_Input'] or 'ERROR'
        break


NewGameWindowGame_Name.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Page 4 [SteamID3] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if glob.glob(".\Variables\SteamID3.txt"): #if file is alredy available
    subprocess.Popen([r".\TTS\NewGame\Page4.2.py"], shell=True, creationflags=subprocess.SW_HIDE)
    print("\n\n\n\nUsing The last SteamID3 That you inputed. \nIf you want to reset it than del the 'SteamID3.txt' File")
    #open file here
    SteamID3File = open(".\Variables\SteamID3.txt", "r")
    steamID3 = SteamID3File.readline()
    SteamID3File.close


else:

    subprocess.Popen([r".\TTS\NewGame\Page4.py"], shell=True, creationflags=subprocess.SW_HIDE)
    # print("\n\n\n\nNow I need your steamID3 without the '[]' OR 'U:1:'\nUse steamid.io to get yous\n\nRemeber! DO NOT INCLUDE THE '[]' OR 'U:1:'")

    NewGameLayoutSteamID3 = [
    [sg.Text("If you want to reset your saved SteamID3, you can delete the 'SteamID3.txt File'", text_color='DarkGray')],
    [sg.Text('\nNow I need your steamID3', font=('', 16))],
    [sg.Text("! Without the following !", text_color='Red', font=('impact', 20))],
    [sg.Text("[]", text_color='black', background_color='white')],
    [sg.Text("U:1:", text_color='black', background_color='white')],
    [sg.Text("! IF YOU DO IT WILL ERROR THE CODE AND NOT WORK !\n", text_color='Red', font=('impact', 20))],
    [sg.Text("Use steamid.io to get your SteamID3\n", font=('Helvitica', 20))],
    [sg.Text("Original SteamID3 > [U:1:123456789]", justification='center')],
    [sg.Text("SteamID3 You Should Use > 123456789", justification='center')],
    [sg.Text("SteamID3 >", justification='Right') , sg.Input(focus=True, key='SteamID3_Input'), sg.Button(button_text='Submit', button_color='Green')],
    ]


    NewGameWindowSteamID3 = sg.Window("SteamID3", NewGameLayoutSteamID3, font=('',14), element_justification='Center')


    while True:
        event, values = NewGameWindowSteamID3.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Submit':
            SteamID3_Value = values['SteamID3_Input'] or 'ERROR'
            break


    NewGameWindowSteamID3.close()


    SteamID3File = open(".\Variables\SteamID3.txt", "x")
    SteamID3File.writelines(SteamID3_Value)
    SteamID3File.close
    SteamID3File = open(".\Variables\SteamID3.txt", "r")
    steamID3 = SteamID3File.readline()
    SteamID3File.close

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Page 5 [Appid] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The Long term plan for this is to make a database of all the Cog's and let the user select the one thay want (with the option of manul input)
# For now though I want the program to just work so it will only be manul input

subprocess.Popen([r".\TTS\NewGame\Page5.py"], shell=True, creationflags=subprocess.SW_HIDE)

NewGameLayoutAppid = [
    [sg.Text("If you want to reset your saved SteamID3, you have to delete the 'SteamID3.txt File'", text_color='DarkGray')],
    [sg.Text('\nNow I need the App ID of the game.')],
    [sg.Text("\nUse steamdb.info to get the AppID of the game you want to save")],
    [sg.Text("App ID >", justification='Right') , sg.Input(focus=True, key='Appid_Input'), sg.Button(button_text='Submit', button_color='Green')],
]


NewGameWindowAppid = sg.Window("App ID", NewGameLayoutAppid, font=('Helvitica',14), element_justification='Center')


while True:
    event, values = NewGameWindowAppid.read(timeout=100)
    if event == sg.WIN_CLOSED:
        exit()
    if event == 'Submit':
        Appid = values['Appid_Input'] or 'ERROR'
        break


NewGameWindowAppid.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Page ? [OS Bit Prosesing] ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is automatic so no user input is required

if glob.glob(".\Variables\Bit64.txt"): #if file is alredy available
    print("64bit")
    print("Allredy run")
    OS_32_or_64 = "64"

elif glob.glob(".\Variables\Bit32.txt"): #if file is alredy available
    print("32bit")
    print("Allredy run")
    OS_32_or_64 = "32"

else: # Finds out what OSbit it is

    OSbit = platform.machine().endswith('64')

    print(OSbit)

    def Bit64():

        Bit1 = open(".\Variables\Bit64.txt", "x")
        Bit1.writelines("64Bit OS, the beast one!")
        Bit1.close
        print("64bit")

        OS_32_or_64 = "64"

    def Bit32():

        Bit2 = open(".\Variables\Bit32.txt", "x")
        Bit2.writelines("32Bit OS or x86")
        Bit2.close
        print("32bit")

        OS_32_or_64 = "32"

# Bit Detections -----------------------
    if OSbit == True:
        print("this is 64bit")
        Bit64()
        OS_32_or_64 = "64"

    elif OSbit == False:
        print("this is not 64bit")
        Bit32()
        OS_32_or_64 = "32"

    else:
        subprocess.Popen([r".\TTS\NewGame\BitOsError.py"], shell=True, creationflags=subprocess.SW_HIDE)

        print("\nThe program cannot detect the os bit!")
        print("Make sure that you are running this program in windows!")
        print("If you are, and want to force the program to continue!")
        print("Make a .txt file in the Variables directory with the architecturey you are running in!")
        print("Example: Bit32.txt or Bit64.txt!")

        input("Press enter to Exit")
        exit()


#----------------------------------------------------- Code Bulder --------------------------------------------------------------------------------------------------------------

# The file to read from
BassCode_File = open(".\DCogSST\.BassCode.py", "r")

# The file in RAW str with lines, so its like a copy paste!
BassCode_Str = BassCode_File.readlines()

BassCode_File.close()


NewGame = open(".\DCogSST\CogSST-" + (Game_Name) + ".py", "w")

NewGame.writelines(BassCode_Str)

NewGame.close()


BassCode_Str[14] ="RootDir = r'" +(RootDir) +"'\n"

BassCode_Str[17] ="Game_Name = r'" +(Game_Name) +"'\n"

BassCode_Str[22] ="steamID3 = " +(steamID3) +"\n"

BassCode_Str[26] ="Appid = " +(Appid) +"\n"

BassCode_Str[29] ="OS_32_or_64 = " +(OS_32_or_64) +"\n"

NewGame = open(".\DCogSST\CogSST-" + (Game_Name) + ".py", "w")

new_file_contents = "".join(BassCode_Str)

NewGame.write(new_file_contents)
NewGame.close()

#----------------------------------------------------- Back to Menu ---------------------------------------------------------------------


run_path(path_name='.\DCogSST\.NewGame.py')

