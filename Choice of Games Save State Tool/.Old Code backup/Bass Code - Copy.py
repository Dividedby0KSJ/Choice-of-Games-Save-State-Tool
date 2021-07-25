print("This file is only to be used to make new gmaes in the 'CoG_ALL_IN_ONE' .py code")
anykey = input("this code will exit on 'Enter' press")
exit
import datetime, os, shutil
Game_Menu = print("You dont know what you are doing")
#----------------------------------------------------- PATHS & TIME -------------------------------------------------------

#The Dir where the saves(Games) will be added
RootDir = r"D:/VSCode Workplace/CoG Save manager"

#Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()

#-------------------------------------------------------- Bass Code -------------------------------------------------------


#Basicly it the subfolder that the time and date folder is going to go in.
Game_Name_SaveSubFolder = r"Game_Name/"

#Path to the games Save Files, It might be difrent on other PC's
Game_Name_SavePath = r"C:\Program Files (x86)\Steam\userdata\160046958\Game\remote"

#Menu to save, load, Game Menu and Exit program
def Game_Name_Menu():
    print("\n\n99. Exit")
    print("0.Game Menu")
    print("1. Save")
    print("2. Load")

    Choice = int(input("Save or Load? > "))
    if Choice == 99:
        exit

    elif Choice == 0:
        print("Back to Game Menu")
        Game_Menu()
    
    elif Choice == 1: #Save
        print("Save")
        
        #Save function, make a  folder with the date and time
        def Game_Name_Save():

            #Ask user for input on the folders Suffix
            SaveName = input("What is the Save Name? ")

            #this is all the aguments above combined into one so shutil and os can make a folder and save
            Game_Name_NewBackupPath = Game_Name_SaveSubFolder + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

            print("Copying Game_Name Instance to Game_Name Backup Folder\nPlease wait")

            os.chdir(RootDir)

            os.makedirs(Game_Name_NewBackupPath)

            shutil.copytree(src=Game_Name_SavePath,
                            dst=Game_Name_NewBackupPath, dirs_exist_ok=True)

            anykey = input("Press the 'Enter' key to go back to the menu")
            Game_Name_Menu()

        Game_Name_Save()

    elif Choice == 2: #Load
        print("Load")

        def Game_Name_Load():
            os.chdir(Game_Name_SaveSubFolder)
            for n, each in enumerate(os.listdir()):
                print(n, each)
            ask = int(input("Number? > "))
            Game_Name_RestoreFolderName = os.listdir()[ask]
            print(Game_Name_RestoreFolderName, " is selected ")
            Game_Name_RestoreFolderPath = RootDir + "/" + Game_Name_SaveSubFolder + Game_Name_RestoreFolderName
            print(Game_Name_RestoreFolderPath, " is the folder Path ")
            
            shutil.copytree(src=Game_Name_RestoreFolderPath,
                            dst=Game_Name_SavePath, dirs_exist_ok=True)
            anykey = input("Press the 'Enter' key to go back to the menu")
            Game_Name_Menu()

        Game_Name_Load()

    else:
        print("\n\nInvalid Answer\n\n")
        Game_Name_Menu()
