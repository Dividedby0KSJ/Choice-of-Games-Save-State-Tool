import datetime, os, shutil, pyttsx3, subprocess
import PySimpleGUI as sg
from time import sleep
sg.theme('Black')   # PySimpleGUI Theme

#------------------------------------------------------- User Input -------------------------------------------------------

# The Dir where the save states will be added
RootDir = r"C:/Users/Divided_By_Zero/.Git/Choice-of-Games-Save-State-Tool/Choice of Games Save State Tool/DCogSST"

# The games name or what you want the program to call the game
Game_Name = r"ASS"

# This is you steam ID 3, for exampil yous might look like [U:1:123456789] you need the last set of numbers, not the 'U:1:'
# or the [], so take out the [U:1:] and leave the other numbers and put them in the steamID3 tag
# use this website to get your steamID3: https://steamid.io or https://steamidfinder.com
steamID3 = 160046958

# The Cog App ID of the game you want to manage
# Check this link for the game id's for all of Cog gmames: https://steamdb.info/search/?a=app_keynames&type=-1&keyname=23&operator=3&keyvalue=Choice+of+Games
Appid = 800620
# put here wether your os is 32bit or 64bit | put ether 32 or 64 as just numbers, leave out the "bit"
OS_32_or_64 = 64

#-------------------------------------------------------- Save Path -------------------------------------------------------

if OS_32_or_64 == 64:
    print("OS is 64bit \n")
    Save_Path = r"C:/Program Files (x86)/Steam/userdata/"+ str(steamID3) +"/"+ str(Appid) +"/remote"

#-------------------------------------------------------- Variable's -------------------------------------------------------

# Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()

# Basicly it the subfolder that the time and date folder is going to go in.
Save_SubFolder = Game_Name + r"/"

#-------------------------------------------------------- Save -------------------------------------------------------


def Game_Save(): 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Game_SaveLayout1 = [
        [sg.Text("The 'Save Name' is a name for identifying the save state.\nIt can be anything or nothing.\nIts up to you.", justification="center")],
        [sg.Text("Save Name >", justification="Right"), sg.Input(focus=True, key="SaveName_Input"), sg.Button(button_text="Submit", button_color="Green")],
    ]


    Game_SaveWindow = sg.Window(Game_Name + " Save", Game_SaveLayout1, element_justification='Center', font=("Roboto", 20))

    while True:
        event, values = Game_SaveWindow.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Submit':
            SaveName = values['SaveName_Input'] or 'NA'
            break

    Game_SaveWindow.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    # this is all the aguments above combined into one so shutil and os can make a folder and save
    New_Backup_Path = Save_SubFolder + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

    Game_SaveLayout2 = [
        [sg.Text("Copying " + (Game_Name) + " Instance to " + (Game_Name) + " Backup Folder\nPlease wait")]
    ]

    print("Copying " + (Game_Name) + " Instance to " + (Game_Name) + " Backup Folder\nPlease wait")

    Game_SaveWindow = sg.Window(Game_Name + " Save", Game_SaveLayout2, element_justification='Center', font=("Roboto", 20))

    while True:
        event, values = Game_SaveWindow.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        sleep(1)
        break

    Game_SaveWindow.close()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    os.chdir(RootDir)

    os.makedirs(New_Backup_Path)

    shutil.copytree(src=Save_Path,
                    dst=New_Backup_Path, dirs_exist_ok=True)


    # anykey = input("Press the 'Enter' key to go back to the menu")

    Game_SaveLayout3 = [
        [sg.Text("Press the 'Continue' button to go back to the menu")],
        [sg.Button(button_text="Continue", key="Continue")],
    ]

    Game_SaveWindow = sg.Window(Game_Name + " Save", Game_SaveLayout3, element_justification='Center', font=("Roboto", 20))

    while True:
        event, values = Game_SaveWindow.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Continue':
            break

    Game_SaveWindow.close()


    Game_SaveLoad_Menu()


#-------------------------------------------------------- Load -------------------------------------------------------


def Game_Load():

    Game_LoadLayout1 = [
        [sg.Text("Use the file browser to open the folder (Save State) that you want to restore")],
        [sg.Input(key="Restore_Folder_Path_Input", default_text=(RootDir + "/" + Save_SubFolder + "Save State Folder")), sg.FolderBrowse('Save State Folder', button_color='#009dff', initial_folder=(RootDir + "/" + Save_SubFolder)), sg.Button(button_text='Submit', button_color='Green')]
    ]


    Game_LoadWindow = sg.Window("Load", Game_LoadLayout1, element_justification='Center', font=("Roboto", 20))

    while True:
        event, values = Game_LoadWindow.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Submit':
            Restore_Folder_Path = values['Restore_Folder_Path_Input'] or 'ERROR'
            break

    Game_LoadWindow.close()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    os.chdir(RootDir)

    os.chdir(Save_SubFolder)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Game_LoadLayout2 = [
        [sg.Text("Are you sure?")],
        [sg.Button(button_text="Yes"), sg.Button(button_text="No")],
    ]

    Game_LoadWindow = sg.Window("Load", Game_LoadLayout2, element_justification='Center', font=("Roboto", 20))

    while True:
        event, values = Game_LoadWindow.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Yes':
            break
        if event == 'No':
            Game_LoadWindow.close()
            Game_SaveLoad_Menu()

    Game_LoadWindow.close()


    shutil.copytree(src=Restore_Folder_Path,
                    dst=Save_Path, dirs_exist_ok=True)


    Game_LoadLayout3 = [
        [sg.Text("Press the 'Continue' button to go back to the menu")],
        [sg.Button(button_text="Continue", key="Continue")],
    ]

    Game_LoadWindow = sg.Window("Load", Game_LoadLayout3, element_justification='Center', font=("Roboto", 20))

    while True:
        event, values = Game_LoadWindow.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Continue':
            break

    Game_LoadWindow.close()



    Game_SaveLoad_Menu()



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def Game_SaveLoad_Menu():

    Game_SaveAndLoad_MenuLayout = [
        [sg.Text("To close the program,\nJust close the window.", font=("arial", 20))],
        [sg.Button(button_text="Save", key="Save", button_color="#4dff00"), sg.Button(button_text="Load", key="Load", button_color="#000dff")]
    ]


    Game_SaveAndLoad_MenuWindow = sg.Window(Game_Name + " Save and Load Menu", Game_SaveAndLoad_MenuLayout, font=("Roboto", 50), element_justification='center')

    while True:
        event, values = Game_SaveAndLoad_MenuWindow.read(timeout=100)
        if event == sg.WIN_CLOSED:
            exit()
        if event == 'Save':
            print("Save")
            Game_SaveAndLoad_MenuWindow.close()
            Game_Save()
        if event == 'Load':
            print("Load")
            Game_SaveAndLoad_MenuWindow.close()
            Game_Load()

Game_SaveLoad_Menu()
