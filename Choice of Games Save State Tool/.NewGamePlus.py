import pyttsx3
TTSEngine = pyttsx3.init()
TTSEngine.setProperty('rate', 190)
#-----------------------------------


print("Wellcom to the game sripts maker! \nI am dev.")
print("I need to ask a few things to make your Cog game compatable with this tool!")




#-----------------------------------

RootDir = input(("RootDir\n>"))

Game_Name = input(("Game Name\n>"))

steamID3 = input(("steamID3\n>"))

Appid = input(("Appid\n>"))

OS_32_or_64 = input(("OS_32_or_64\n>"))

#-----------------------------------

# The file to read from
BassCode_File = open("Choice of Games Save State Tool\Bass Code V2.py")

# The file in RAW str with lines, so its like a copy paste!
BassCode_Str = BassCode_File.readlines()

BassCode_File.close()


NewGame = open("Choice of Games Save State Tool\CogSST-" + (Game_Name) + ".py", "w")

NewGame.writelines(BassCode_Str)

NewGame.close()


BassCode_Str[18] ="    " + "RootDir = r'" +(RootDir) +"'\n"

BassCode_Str[21] ="    " + "Game_Name = r'" +(Game_Name) +"'\n"

BassCode_Str[26] ="    " + "steamID3 = " +(steamID3) +"\n"

BassCode_Str[30] ="    " + "Appid = " +(Appid) +"\n"

BassCode_Str[33] ="    " + "OS_32_or_64 = " +(OS_32_or_64) +"\n"

NewGame = open("Choice of Games Save State Tool\CogSST-" + (Game_Name) + ".py", "w")

new_file_contents = "".join(BassCode_Str)

NewGame.write(new_file_contents)
NewGame.close()