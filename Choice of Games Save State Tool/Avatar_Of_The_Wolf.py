import datetime, os, shutil, runpy
Stop = 0
#------------------------------------------------------- User Input -------------------------------------------------------

#The Dir where the saves(Games) will be added
RootDir = r"D:/VSCode Workplace/CoG Save manager"

#the games name or what you want the program to call the game
Game_Name = r"Avatar of the Wolf"

#Path to the games Save Files, It might be difrent on other PC's. Add you steam Numbers and game numbers
Save_Path = r"C:/Program Files (x86)/Steam/userdata/160046958/643570/remote"

#---------------------------------------------------------- Time -------------------------------------------------------

#Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()

#-------------------------------------------------------- Bass Code -------------------------------------------------------


#Basicly it the subfolder that the time and date folder is going to go in.
Save_SubFolder = Game_Name + r"/"


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
        
        #Save function, make a  folder with the date and time
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

        Game_Save()

    elif Choice == 2: #Load
        print("Load")

        def Game_Load():
            os.chdir(Save_SubFolder)
            for n, each in enumerate(os.listdir()):
                print(n, each)
            ask = int(input("Number? > "))
            Restore_Folder_Name = os.listdir()[ask]
            print(Restore_Folder_Name, " is selected ")
            Restore_Folder_Path = RootDir + "/" + Save_SubFolder + Restore_Folder_Name
            print(Restore_Folder_Path, " is the folder Path ")

            #See's if you want to load that file
            Confirm_Load = int(input("\nDo you want to continue? \n 1. Yes \n 2. No \n > "))

            if Confirm_Load == 1:
                print("Loading Game")

            elif Confirm_Load == 2:
                print("Ok :)")
                

            else:
                print("Invalid Anser")
                Confirm_Load()
            
            
            shutil.copytree(src=Restore_Folder_Path,
                            dst=Save_Path, dirs_exist_ok=True)
            anykey = input("Press the 'Enter' key to go back to the menu")
            
            

        Game_Load()

    else:
        print("\n\nInvalid Answer\n\n")
        Game_SaveLoad_Menu()


#-------------------------------------------------------- Code Start -------------------------------------------------------

print("this is the Save Load menu for " + (Game_Name))


if Stop == 1:
    print()

elif Stop == 0:
    Game_SaveLoad_Menu()
    Game_SaveLoad_Menu()
    Game_SaveLoad_Menu()
