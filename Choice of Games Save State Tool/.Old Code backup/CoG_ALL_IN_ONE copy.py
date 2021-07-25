import datetime, os, shutil, runpy


import Hellotxt
#Hellotxt.A1()
#Hellotxt.A2()

#this is the Menu... duhh
def Game_Menu():
    print("\n\n0. Exit")
    print("1. Choice of the Dragon")
    print("2. Fox Spirit")
    print("3. Werewolves Haven Rising")
    print("4. Test file")

    Choice = int(input("Witch Game Do You Want To Mange > "))
    if Choice == 0:
        exit

    elif Choice == 1:
        CoT_Dragon_Menu()

    elif Choice == 2:
        Fox_Spirit_Menu()

    elif Choice == 3:
        Werewolves_Haven_Rising_Menu()

    elif Choice == 4:
        runpy.run_module(mod_name='TestF')
   
    else:
        print("\n\nInvalid Answer\n\n")
        Game_Menu()


#----------------------------------------------------- PATHS & TIME -------------------------------------------------------

#The Dir where the saves(Games) will be added
RootDir = r"D:/VSCode Workplace/CoG Save manager"

#Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()


#-------------------------------------------------- Choice of the Dragon --------------------------------------------------

#Basicly it the subfolder that the time and date folder is going to go in.
CoT_Dragon_SaveSubFolder = r"Choice of the Dragon/"

#Path to the games Save Files, It might be difrent on other PC's
CoT_Dragon_SavePath = r"C:\Program Files (x86)\Steam\userdata\160046958\1044630\remote"

#Dragon Menu to save, load, Game Menu and Exit program
def CoT_Dragon_Menu():
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
        def CoT_Dragon_Save():

            #Ask user for input on the folders Suffix
            SaveName = input("What is the Save Name? ")

            #this is all the aguments above combined into one so shutil and os can make a folder and save
            CoT_Dragon_NewBackupPath = CoT_Dragon_SaveSubFolder + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

            print("Copying Choice of the Dragon Instance to Fox Spirit Backup Folder\nPlease wait")

            os.chdir(RootDir)

            os.makedirs(CoT_Dragon_NewBackupPath)

            shutil.copytree(src=CoT_Dragon_SavePath,
                            dst=CoT_Dragon_NewBackupPath, dirs_exist_ok=True)

            anykey = input("Press the 'Enter' key to go back to the menu")
            CoT_Dragon_Menu()

        CoT_Dragon_Save()

    elif Choice == 2: #Load
        print("Load")

        def CoT_Dragon_Load():
            os.chdir(CoT_Dragon_SaveSubFolder)
            for n, each in enumerate(os.listdir()):
                print(n, each)
            ask = int(input("Number? > "))
            CoT_Dragon_RestoreFolderName = os.listdir()[ask]
            print(CoT_Dragon_RestoreFolderName, " is selected ")
            CoT_Dragon_RestoreFolderPath = RootDir + "/" + CoT_Dragon_SaveSubFolder + CoT_Dragon_RestoreFolderName
            print(CoT_Dragon_RestoreFolderPath, " is the folder Path ")
            
            shutil.copytree(src=CoT_Dragon_RestoreFolderPath,
                            dst=CoT_Dragon_SavePath, dirs_exist_ok=True)
            anykey = input("Press the 'Enter' key to go back to the menu")
            CoT_Dragon_Menu()

        CoT_Dragon_Load()

    else:
        print("\n\nInvalid Answer\n\n")
        CoT_Dragon_Menu()


#------------------------------------------------------ Fox Spirit --------------------------------------------------------

#Basicly it the subfolder that the time and date folder is going to go in.
Fox_Spirit_SaveSubFolder = r"Fox Spirit/"

#Path to the games Save Files, It might be difrent on other PC's
Fox_Spirit_SavePath = r"C:\Program Files (x86)\Steam\userdata\160046958\1324420\remote"

def Fox_Spirit_Menu():
    print("\n\n99. Exit")
    print("0.Main Menu")
    print("1. Save")
    print("2. Load")

    Choice = int(input("Save or Load? > "))
    if Choice == 99:
        exit

    elif Choice == 0:
        print("Back to manin menu")
        Game_Menu()
    
    elif Choice == 1: #Save
        print("Save")

        def Fox_Spirit_Save():

            #Ask user for input on the folders Suffix
            SaveName = input("What is the Save Name? ")

            #this is all the aguments above combined into one so shutil and os can make a folder and save
            Fox_Spirit_NewBackupPath = Fox_Spirit_SaveSubFolder + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

            print("Copying Fox Spirit Instance to Fox Spirit Backup Folder\nPlease wait")

            os.chdir(RootDir)

            os.makedirs(Fox_Spirit_NewBackupPath)

            shutil.copytree(src=Fox_Spirit_SavePath,
                            dst=Fox_Spirit_NewBackupPath, dirs_exist_ok=True)

            anykey = input("Press the 'Enter' key to go back to the menu")
            Fox_Spirit_Menu()
        Fox_Spirit_Save()

    elif Choice == 2: #Load
        print("Load")

        def Fox_Spirit_Load():
            os.chdir(Fox_Spirit_SaveSubFolder)
            for n, each in enumerate(os.listdir()):
                print(n, each)
            ask = int(input("Number? > "))
            Fox_Spirit_RestoreFolderName = os.listdir()[ask]
            print(Fox_Spirit_RestoreFolderName, " is selected ")
            Fox_Spirit_RestoreFolderPath = RootDir + "/" + Fox_Spirit_SaveSubFolder + Fox_Spirit_RestoreFolderName
            print(Fox_Spirit_RestoreFolderPath, " is the folder Path ")
            
            shutil.copytree(src=Fox_Spirit_RestoreFolderPath,
                            dst=Fox_Spirit_SavePath, dirs_exist_ok=True)
            anykey = input("Press the 'Enter' key to go back to the menu")
            Fox_Spirit_Menu()
        Fox_Spirit_Load()

    else:
        print("\n\nInvalid Answer\n\n")
        Fox_Spirit_Menu()


#-------------------------------------------------------- Werewolves Haven Rising -------------------------------------------------------


#Basicly it the subfolder that the time and date folder is going to go in.
Werewolves_Haven_Rising_SaveSubFolder = r"Werewolves Haven Rising/"

#Path to the games Save Files, It might be difrent on other PC's
Werewolves_Haven_Rising_SavePath = r"C:\Program Files (x86)\Steam\userdata\160046958\885120\remote"

#Menu to save, load, Game Menu and Exit program
def Werewolves_Haven_Rising_Menu():
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
        def Werewolves_Haven_Rising_Save():

            #Ask user for input on the folders Suffix
            SaveName = input("What is the Save Name? ")

            #this is all the aguments above combined into one so shutil and os can make a folder and save
            Werewolves_Haven_Rising_NewBackupPath = Werewolves_Haven_Rising_SaveSubFolder + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

            print("Copying Werewolves Haven Rising Instance to Fox Spirit Backup Folder\nPlease wait")

            os.chdir(RootDir)

            os.makedirs(Werewolves_Haven_Rising_NewBackupPath)

            shutil.copytree(src=Werewolves_Haven_Rising_SavePath,
                            dst=Werewolves_Haven_Rising_NewBackupPath, dirs_exist_ok=True)

            anykey = input("Press the 'Enter' key to go back to the menu")
            Werewolves_Haven_Rising_Menu()

        Werewolves_Haven_Rising_Save()

    elif Choice == 2: #Load
        print("Load")

        def Werewolves_Haven_Rising_Load():
            os.chdir(Werewolves_Haven_Rising_SaveSubFolder)
            for n, each in enumerate(os.listdir()):
                print(n, each)
            ask = int(input("Number? > "))
            Werewolves_Haven_Rising_RestoreFolderName = os.listdir()[ask]
            print(Werewolves_Haven_Rising_RestoreFolderName, " is selected ")
            Werewolves_Haven_Rising_RestoreFolderPath = RootDir + "/" + Werewolves_Haven_Rising_SaveSubFolder + Werewolves_Haven_Rising_RestoreFolderName
            print(Werewolves_Haven_Rising_RestoreFolderPath, " is the folder Path ")
            
            shutil.copytree(src=Werewolves_Haven_Rising_RestoreFolderPath,
                            dst=Werewolves_Haven_Rising_SavePath, dirs_exist_ok=True)
            anykey = input("Press the 'Enter' key to go back to the menu")
            Werewolves_Haven_Rising_Menu()

        Werewolves_Haven_Rising_Load()

    else:
        print("\n\nInvalid Answer\n\n")
        Werewolves_Haven_Rising_Menu()


#-------------------------------------------------- the code starts here --------------------------------------------------


Game_Menu()


#--------------------------------------------------- the code ends here ---------------------------------------------------