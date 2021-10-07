# print("This file is only to be used to make new gmaes in the 'CoG_ALL_IN_ONE' .py code")
# anykey = input("this code will run on 'Enter' press")
# exit()
#-------------------------------------------------- Copy all code below -------------------------------------------------------
import datetime, os, shutil, pyttsx3, subprocess
from runpy import run_module
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
    TTSEngine.say ((Error_OsBit) + ". Now Closing")
    TTSEngine.runAndWait()
    print((Error_OsBit) + "\nNow closing")
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

    # Ask user for input on the folders Suffix
    SaveName = input("\n >")
    

    # this is all the aguments above combined into one so shutil and os can make a folder and save
    New_Backup_Path = Save_SubFolder + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName


    TTSEngine.say("Copying " + (Game_Name) + " Instance to " + (Game_Name) + " Backup Folder. Please wait")
    print("Copying " + (Game_Name) + " Instance to " + (Game_Name) + " Backup Folder\nPlease wait")
    TTSEngine.runAndWait()


    os.chdir(RootDir)

    os.makedirs(New_Backup_Path)

    shutil.copytree(src=Save_Path,
                    dst=New_Backup_Path, dirs_exist_ok=True)


    TTSEngine.say("Done!")
    TTSEngine.runAndWait()
    anykey = input("Press the 'Enter' key to go back to the menu")
    Game_SaveLoad_Menu()

#-------------------------------------------------------- Load -------------------------------------------------------

# Load Function, list the saved folders in the [ RootDir + Save_SubFolder ] and ask's the users witch to select to load
def Game_Load():

    os.chdir(RootDir)

    os.chdir(Save_SubFolder)

    for n, each in enumerate(os.listdir()):
        print(n, each)

    ask = int(input("Number? > "))

    Restore_Folder_Name = os.listdir()[ask]

    Restore_Folder_Path = RootDir + "/" + Save_SubFolder + Restore_Folder_Name

    # This gets rid of the numbers in the Restore_Folder_Name so the TTS only says the Save Name
    Restore_Folder_TTS = ''.join([i for i in Restore_Folder_Name if not i.isdigit()])


    TTSEngine.say((Restore_Folder_TTS) + " is selected ")
    print("\n" + (Restore_Folder_Name) + " is selected ")

    TTSEngine.say("This is the folder path of what you selected.")
    print("\n '" + (Restore_Folder_Path) + "'\nIs the folder Path of what you selected. ")

    TTSEngine.runAndWait()

    TTSEngine.say("Are you sure?")
    print("Are you sure? \n")

    TTSEngine.runAndWait()

    Load_Confirm = input(("Yes [Y] Or No [N] \n"))

    if Load_Confirm == "y" or Load_Confirm == "Y":
        TTSEngine.say("Continuing")
        print("'Yes'")
        TTSEngine.runAndWait()

    elif Load_Confirm == "n" or Load_Confirm == "N":
        TTSEngine.say("Cancelling")
        print("'No'")
        TTSEngine.runAndWait()
        Game_SaveLoad_Menu()

    else:
        TTSEngine.say("Invalid Answer!")
        print("\n\nInvalid Answer!")
        TTSEngine.runAndWait()
        Game_Load()

    # print(Load_Confirm) # This is a debug, ignor this
    
    shutil.copytree(src=Restore_Folder_Path,
                    dst=Save_Path, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Game_SaveLoad_Menu()

    
#-------------------------------------------------------- Menue -------------------------------------------------------

# Menu to save, load, Game Menu and Exit program
def Game_SaveLoad_Menu():
    print("\n99. Exit")
    print("0.Game Menu")
    print("1. Save")
    print("2. Load")

    # Shutdown program
    Choice = int(input("Save or Load? > "))
    if Choice == 99:
        run_module(mod_name='0CogSST-GoodByetxt')

    # Game Menu
    elif Choice == 0:
        print("Back to Game Menu")
        #runs the TTS engin in another termainal to prevent it from interupting the text scrole
        subprocess.Popen(['TTS Lines/BackToGameMenu.py'], shell=True, creationflags=subprocess.SW_HIDE)
        run_module(mod_name='CogMenu')

    # Save
    elif Choice == 1:
        TTSEngine.say("Save, What is the Save Name?")
        print("Save \nWhat is the Save Name?")
        TTSEngine.runAndWait()
        Game_Save()

    # Load
    elif Choice == 2:
        TTSEngine.say("Load")
        print("Load")
        TTSEngine.runAndWait()
        Game_Load()

    else:
        TTSEngine.say("Invalid Answer!")
        print("\n\nInvalid Answer\n\n")
        TTSEngine.runAndWait()
        Game_SaveLoad_Menu()

#-------------------------------------------------------- Code Start -------------------------------------------------------

TTSEngine.say("This is the Save Load menu for " + (Game_Name))
print("\033[04mThis is the Save Load menu for " + (Game_Name) + "\033[0m")
TTSEngine.runAndWait()

Game_SaveLoad_Menu()
