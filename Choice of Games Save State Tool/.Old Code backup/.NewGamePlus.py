import pyttsx3, platform, glob
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)
#-----------------------------------


print("Wellcom to the game sripts maker! \nI am dev.")
print("I need to ask a few things to make your Cog game compatable with this tool!")
print("\nPlease look at 'Your Variables & Help.txt' to get more info!\n")


#-----------------------------------

if glob.glob("RootDir.txt"): #if file is alredy available
    print("\n\n\n\nUsing The last RootDir That you inputed. \nIf you want to reset it than del the 'RootDir.txt' File")
    #open file here
    RootDirFile = open(".\RootDir.txt", "r")
    RootDir = RootDirFile.readline()
    RootDirFile.close
    # ass

else:
    print("\nFirst I'm Going to need the path you want to store your save files\n")
    print("E.g: >>> C:/Users/YourUserName/Saved Games/CogSST <<<\n")
    print("its caled in this code RootDir. So please type the path without '' {Quotation Marks}\n And with '/' insead of 'BackSlash' \n")
    print("\nOh And this is semi-permanent!! \nSo if you want to change this than you must delete the 'RootDir.txt' File as well as re-make your game save/load files\n")
    # RootDir = input(("RootDir\n>"))
    # #assert
    RootDirFile = open(".\RootDir.txt", "x")
    RootDirFile.writelines(input(("RootDir\n>")))
    RootDirFile.close
    RootDirFile = open(".\RootDir.txt", "r")
    RootDir = RootDirFile.readline()
    RootDirFile.close


print("\n\n\n\nNow I need the name of the game or what you want the code to call the game.\n")
print("!YOU CANNOT USE! The following reserved characters: < (less than) > (greater than) \n : (colon) [I cant show you it] (double quote) / (forward slash) \ (backslash) | (vertical bar or pipe) \n ? (question mark) * (asterisk) \n IF YOU DO IT WILL ERROR THE CODE AND NOT WORK\n")
print("E.g: >>> Werewolves Haven Rising [O.G Name (Werewolves: Haven Rising)] <<<\n")
Game_Name = input(("Game Name\n>"))

if glob.glob("SteamID3.txt"): #if file is alredy available
    print("\n\n\n\nUsing The last SteamID3 That you inputed. \nIf you want to reset it than del the 'SteamID3.txt' File")
    #open file here
    SteamID3File = open(".\SteamID3.txt", "r")
    steamID3 = SteamID3File.readline()
    SteamID3File.close


else:

    print("\n\n\n\nNow I need your steamID3 without the '[]' OR 'U:1:'\nUse steamid.io to get yous\n\nRemeber! DO NOT INCLUDE THE '[]' OR 'U:1:'")
    # steamID3 = input(("steamID3\n>"))
    SteamID3File = open(".\SteamID3.txt", "x")
    SteamID3File.writelines(input(("steamID3\n>")))
    SteamID3File.close
    SteamID3File = open(".\SteamID3.txt", "r")
    steamID3 = SteamID3File.readline()
    SteamID3File.close

print("\n\n\n\nOK this is (almost) the last one!\nI need the Appid of the game.\nGoto steamdb.info and serch your games name and copy paste the App ID here!")
Appid = input(("Appid\n>"))

# print("\n\n\n\nOK. OK. OK... THIS is the last one and it is the simplest one\nWhat is your windows os bit? it can only be 32 or 64 (or the code wont work)\n and you can only input 32 or 64\nIf you dont know, open 'System Information' and look under 'System type' if it says x64-based than you are 64.\n")
# OS_32_or_64 = input(("OS_32_or_64\n>"))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if glob.glob("Bit64.txt"): #if file is alredy available
    print("64bit")
    OS_32_or_64 = "64"

elif glob.glob("Bit32.txt"): #if file is alredy available
    print("32bit")
    OS_32_or_64 = "32"

else: # Finds out what OSbit it is

    OSbit = platform.machine().endswith('64')

    # print(OSbit)

#---------------------------------------------------------------- Bit Prosesing -------------------------------------------------------
    def Bit64():

        Bit1 = open(".\Bit64.txt", "x")
        Bit1.writelines("64Bit OS, the beast one!")
        Bit1.close

    def Bit32():

        Bit2 = open(".\Variables\Bit32.txt", "w")
        Bit2.writelines("32Bit OS or x86")
        Bit2.close
#----------------------------------------------------- Bit Detections ---------------------------------------------------------------


    if OSbit == True:
        print("this is 64bit")
        Bit64()

    elif OSbit == False:
        print("this is not 64bit")
        Bit32()

    else:
        print("this is not 64bit or 32bit \n ERROR: Unknown OSbit")
        exit()

#-----------------------------------

# The file to read from
BassCode_File = open(".\Bass Code V2.py", "r")

# The file in RAW str with lines, so its like a copy paste!
BassCode_Str = BassCode_File.readlines()

BassCode_File.close()


NewGame = open("CogSST-" + (Game_Name) + ".py", "w")

NewGame.writelines(BassCode_Str)

NewGame.close()


BassCode_Str[18] ="    " + "RootDir = r'" +(RootDir) +"'\n"

BassCode_Str[21] ="    " + "Game_Name = r'" +(Game_Name) +"'\n"

BassCode_Str[26] ="    " + "steamID3 = " +(steamID3) +"\n"

BassCode_Str[30] ="    " + "Appid = " +(Appid) +"\n"

BassCode_Str[33] ="    " + "OS_32_or_64 = " +(OS_32_or_64) +"\n"

NewGame = open("CogSST-" + (Game_Name) + ".py", "w")

new_file_contents = "".join(BassCode_Str)

NewGame.write(new_file_contents)
NewGame.close()