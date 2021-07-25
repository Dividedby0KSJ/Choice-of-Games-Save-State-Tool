import datetime, os, shutil

#the folowing is all the definitions for the code to understand where everything is.


#Path to the games Save Files, It might be difrent on other PC's
CoT_Dragon_SavePath = r"C:\Program Files (x86)\Steam\userdata\160046958\1044630\remote"


#Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()


#This is self-explanatory,
#Basicly it the subfolder that the
#time and date folder is going to go in.
GameName = r"Choice of the Dragon/"

RootDir = r"D:/VSCode Workplace/CoG Save manager"


#Save function, make a  folder with the date and time
def CoT_Dragon_Save():

    #Ask user for input on the folders Suffix
    SaveName = input("What is the Save Name? ")

    #this is all the aguments above combined into one so shutil and os can make a folder and save
    CoT_Dragon_NewBackupPath = GameName + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

    print("Copying Choice of the Dragon Instance to Fox Spirit Backup Folder\nPlease wait")

    os.chdir(RootDir)

    os.makedirs(CoT_Dragon_NewBackupPath)

    shutil.copytree(src=CoT_Dragon_SavePath,
                    dst=CoT_Dragon_NewBackupPath, dirs_exist_ok=True)

    anykey = input("Press the 'Enter' key to go back to the menu")
    CoT_Dragon_Menu()


#Load Function   
def CoT_Dragon_Load():
    print("Not working properly yet")
    os.chdir(GameName)
    for n, each in enumerate(os.listdir()):
        print(n, each)
    ask = int(input("Number? > "))
    CoT_Dragon_RestoreFolderName = os.listdir()[ask]
    print(CoT_Dragon_RestoreFolderName, " is selected ")
    CoT_Dragon_RestoreFolderPath = RootDir + "/" + GameName + CoT_Dragon_RestoreFolderName
    print(CoT_Dragon_RestoreFolderPath, " is the folder Path ")
    
    shutil.copytree(src=CoT_Dragon_RestoreFolderPath,
                    dst=CoT_Dragon_SavePath, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    CoT_Dragon_Menu()


#The Menu to run the script
def CoT_Dragon_Menu():
    print("\n\n99. Exit")
    print("0.Main Menu")
    print("1. Save")
    print("2. Load")

    Choice = int(input("Save or Load? > "))
    if Choice == 99:
        exit

    elif Choice == 0:
        print("Back to manin menu")
        exec(open('Main_Script_COG.py').read())
    
    elif Choice == 1:
        print("Save")
        CoT_Dragon_Save()

    elif Choice == 2:
        print("Load")
        CoT_Dragon_Load()

    else:
        print("\n\nInvalid Answer\n\n")
        CoT_Dragon_Menu()


#-------------------------------------------------- the code starts here --------------------------------------------------


CoT_Dragon_Menu()