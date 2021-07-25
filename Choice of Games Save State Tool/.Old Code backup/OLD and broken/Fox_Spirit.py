import datetime, os, shutil

#the folowing is all the definitions for the code to understand where everything is.


#Path to the games Save Files, It might be difrent on other PC's
Fox_Spirit_SavePath = r"C:\Program Files (x86)\Steam\userdata\160046958\1324420\remote"


#Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()


#This is self-explanatory,
#Basicly it the subfolder that the
#time and date folder is going to go in.
GameName = r"Fox Spirit/"

RootDir = r"D:/VSCode Workplace/CoG Save manager"


#Save function, make a  folder with the date and time
def Fox_Spirit_Save():

    #Ask user for input on the folders Suffix
    SaveName = input("What is the Save Name? ")

    #this is all the aguments above combined into one so shutil and os can make a folder and save
    Fox_Spirit_NewBackupPath = GameName + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

    print("Copying Fox Spirit Instance to Fox Spirit Backup Folder\nPlease wait")

    os.chdir(RootDir)

    os.makedirs(Fox_Spirit_NewBackupPath)

    shutil.copytree(src=Fox_Spirit_SavePath,
                    dst=Fox_Spirit_NewBackupPath, dirs_exist_ok=True)

    anykey = input("Press the 'Enter' key to go back to the menu")
    Fox_Spirit_Menu()


#Load Function   
def Fox_Spirit_Load():
    print("Not working properly yet")
    os.chdir(GameName)
    for n, each in enumerate(os.listdir()):
        print(n, each)
    ask = int(input("Number? > "))
    Fox_Spirit_RestoreFolderName = os.listdir()[ask]
    print(Fox_Spirit_RestoreFolderName, " is selected ")
    Fox_Spirit_RestoreFolderPath = RootDir + "/" + GameName + Fox_Spirit_RestoreFolderName
    print(Fox_Spirit_RestoreFolderPath, " is the folder Path ")
    
    shutil.copytree(src=Fox_Spirit_RestoreFolderPath,
                    dst=Fox_Spirit_SavePath, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Fox_Spirit_Menu()


#The Menu to run the script
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
        exec(open('Main_Script_COG.py').read())
    
    elif Choice == 1:
        print("Save")
        Fox_Spirit_Save()

    elif Choice == 2:
        print("Load")
        Fox_Spirit_Load()

    else:
        print("\n\nInvalid Answer\n\n")
        Fox_Spirit_Menu()


#-------------------------------------------------- the code starts here --------------------------------------------------


Fox_Spirit_Menu()