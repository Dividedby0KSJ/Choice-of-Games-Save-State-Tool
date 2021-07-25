import datetime, os, shutil

#the folowing is all the definitions for the code to understand where everything is.

#Path to the games Save Files, It might be difrent on other PC's
Game_SavePath = r"C:\Program Files (x86)\Steam\userdata\160046958\GAME ID\remote"

#Gets the current Date and time "Year-Month-Day Hour.Minute.second"
FileDateAndTime = datetime.datetime.now()

#Ask user for input on the folders Suffix
SaveName = "1" #input("What is the Save Name? ")

#This is self-explanatory,
#Basicly it the subfolder that the
#time and date folder is going to go in.
GameName = r"GAME NAME/"

#this is all the aguments above combined into one so shutil and os can make a folder and save
Game_BackupPath = GameName + FileDateAndTime.strftime('%Y-%m-%d %H.%M.%S ') + SaveName

#this is temporary and is currently only doing the copy function
#(later it will make the folder too and link back to a "load and save" menu)
def Game_Save():
    print("Copying Fox Spirit Instance to Fox Spirit Backup Folder\nPlease wait")
    shutil.copytree(src=Game_SavePath,
                    dst=Game_BackupPath, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to exit")
    exit
    


#-------------------------------------------------- the code starts here --------------------------------------------------