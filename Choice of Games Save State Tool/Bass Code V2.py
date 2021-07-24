print("This file is only to be used to make new gmaes in the 'CoG_ALL_IN_ONE' .py code")
anykey = input("this code will run on 'Enter' press")
#exit()
#-------------------------------------------------- Copy all code below -------------------------------------------------------
import datetime, os, shutil, runpy, sys

i = 0
while i <= 10:

    #------------------------------------------------------- User Input -------------------------------------------------------

    #The Dir where the saves(Games) will be added
    RootDir = r"D:/VSCode Workplace/CoG Save manager"

    #the games name or what you want the program to call the game
    Game_Name = r"Game Name"

    #Path to the games Save Files, It might be difrent on other PC's. Add you steam Numbers and game numbers
    Save_Path = r"C:/Program Files (x86)/Steam/userdata/UserNumbers/Game/remote"

    #-------------------------------------------------------- Variable's -------------------------------------------------------

    #Gets the current Date and time "Year-Month-Day Hour.Minute.second"
    FileDateAndTime = datetime.datetime.now()

    #Basicly it the subfolder that the time and date folder is going to go in.
    Save_SubFolder = Game_Name + r"/"

    #-------------------------------------------------------- Save -------------------------------------------------------               

    #Save function, make a folder with the date and time
    def Game_Save(): 

        #Ask user for input on the folders Suffix
        SaveName = input("What is the Save Name? ")

        #this is all the aguments above combined into one so shutil and os can make a folder and save
        New_Backup_Path = Save_SubFolder + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

        print("Copying " + (Game_Name) + " Instance to " + (Game_Name) + " Backup Folder\nPlease wait")

        os.chdir(RootDir)

        os.makedirs(New_Backup_Path)

        shutil.copytree(src=Save_Path,
                        dst=New_Backup_Path, dirs_exist_ok=True)

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
        print("\n" + (Restore_Folder_Name) + " is selected ")
        Restore_Folder_Path = RootDir + "/" + Save_SubFolder + Restore_Folder_Name
        print("\n '" + (Restore_Folder_Path) + "' is the folder Path ")
        
        shutil.copytree(src=Restore_Folder_Path,
                        dst=Save_Path, dirs_exist_ok=True)
        anykey = input("Press the 'Enter' key to go back to the menu")
        

    #-------------------------------------------------------- Menue -------------------------------------------------------

    #Menu to save, load, Game Menu and Exit program
    def Game_SaveLoad_Menu():
        print("\n\n99. Exit")
        print("0.Game Menu")
        print("1. Save")
        print("2. Load")

        Choice = int(input("Save or Load? > "))
        if Choice == 99:
            runpy.run_module(mod_name='GoodByetxt')

        elif Choice == 0:
            print("Back to Game Menu")
            runpy.run_module(mod_name='CogMenu')

        elif Choice == 1: #Save
            print("Save")
            Game_Save()

        elif Choice == 2: #Load
            print("Load")
            Game_Load()

        else:
            print("\n\nInvalid Answer\n\n")
            Game_SaveLoad_Menu()

    #-------------------------------------------------------- Code Start -------------------------------------------------------

    print("this is the Save Load menu for " + (Game_Name))

    Game_SaveLoad_Menu()
