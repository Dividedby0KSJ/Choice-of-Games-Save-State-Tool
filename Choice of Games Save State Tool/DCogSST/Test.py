import PySimpleGUI as sg
from time import sleep
import os, subprocess, glob

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

sg.theme('Black')   # PySimpleGUI Theme


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Null ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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