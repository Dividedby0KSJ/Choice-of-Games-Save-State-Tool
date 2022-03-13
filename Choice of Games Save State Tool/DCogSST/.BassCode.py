
# There needs to be a blank line at the start of the file, its for the BassCode_Str[#], because you have to use the line number -1 (I dont know why, but you do). 
#-------------------------------------------------- Copy all code below -------------------------------------------------------
import datetime, os, shutil, pyttsx3, subprocess
import PySimpleGUI as sg
from time import sleep

# initialize Text-to-speech engine
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)

#------------------------------------------------------- User Input -------------------------------------------------------

# The Dir where the save states will be added
RootDir = r"C:/Users/User/Saved Games/CogSST"

# The games name or what you want the program to call the game
Game_Name = r"Game Name"

# This is you steam ID 3, for exampil yous might look like [U:1:123456789] you need the last set of numbers, not the 'U:1:'
# or the [], so take out the [U:1:] and leave the other numbers and put them in the steamID3 tag
# use this website to get your steamID3: https://steamid.io or https://steamidfinder.com
steamID3 = 123456789

# The Cog App ID of the game you want to manage
# Check this link for the game id's for all of Cog gmames: https://steamdb.info/search/?a=app_keynames&type=-1&keyname=23&operator=3&keyvalue=Choice+of+Games
Appid = 123456789

# put here wether your os is 32bit or 64bit | put ether 32 or 64 as just numbers, leave out the "bit"
OS_32_or_64 = 0

#-------------------------------------------------------- Save Path -------------------------------------------------------

if OS_32_or_64 == 64:
    print("OS is 64bit \n")
    Save_Path = r"C:/Program Files (x86)/Steam/userdata/"+ str(steamID3) +"/"+ str(Appid) +"/remote"

elif OS_32_or_64 == 32:
    print("OS is 32bit, why tho? \nLike just update to 64bit man\n")
    Save_Path = r"C:/Program Files/Steam/userdata/"+ str(steamID3) +"/"+ str(Appid) +"/remote"

else:
    Error_OsBit = "You need to state wether the OS is 32 bit or 64 bit in the game saveload file!"
    print((Error_OsBit) + "\nNow closing")
    TTSEngine.say ((Error_OsBit) + ". Now Closing")
    TTSEngine.runAndWait()
    exit()

# Path to the games Save Files, It might be difrent on other PC's. Add you steam Numbers and game numbers

# Save_Path = r"C:/Program Files (x86)/Steam/userdata/UserNumbers/Game/remote"

# ^^^^^ this is an overide if you need it, witch you probubly wont, but basicly you just put you steamID3 in "UserNumbers"
# and Appid in "Game". and if you are not 64bit than take out " (x86)".

#-------------------------------------------------------- Variable's -------------------------------------------------------

# Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()

# Basicly it the subfolder that the time and date folder is going to go in.
Save_SubFolder = Game_Name + r"/"

#-------------------------------------------------------- Save -------------------------------------------------------               

# Save function, make a folder with the date and time
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

# Load Function, list the saved folders in the [ RootDir + Save_SubFolder ] and ask's the users witch to select to load
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

    
#-------------------------------------------------------- Menue -------------------------------------------------------

# Menu to save, load, Game Menu and Exit program
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


    # print("1. Save")
    # print("2. Load")

    # Choice = int(input("Save or Load? > "))

    # # Save
    # if Choice == 1:
    #     TTSEngine.say("Save, What is the Save Name?")
    #     print("Save \nWhat is the Save Name?")
    #     TTSEngine.runAndWait()
    #     Game_Save()

    # # Load
    # elif Choice == 2:
    #     TTSEngine.say("Load")
    #     print("Load")
    #     TTSEngine.runAndWait()
    #     Game_Load()

#-------------------------------------------------------- Code Start -------------------------------------------------------

TTSEngine.say("This is the Save Load menu for " + (Game_Name))
print("\033[04mThis is the Save Load menu for " + (Game_Name) + "\033[0m")
TTSEngine.runAndWait()

Game_SaveLoad_Menu()
