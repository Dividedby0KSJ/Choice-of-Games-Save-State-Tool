# The file to read from
BassCode_File = open("Bass Code V2.py")

# The file in RAW str with lines, so its like a copy paste!
BassCode_Str = BassCode_File.readlines()

# Fuckmypussy = open("ass.txt", "w")
# Fuckmypussy.writelines(BassCode_Str)
# Fuckmypussy.close()
# exit()

BassCode_File.close()

NewGame = open("test_file.py", "w")

NewGame.writelines(BassCode_Str)

NewGame.close()

# line +1, so 0 is aculy 1 | this is what to add to the prefex of that line.
#BassCode_Str[18] ="    #Null my dick\n"


RootDir = input(("RootDir\n>"))
BassCode_Str[18] ="    " + "RootDir = r'" +(RootDir) +"'\n"


Game_Name = input(("Game Name\n>"))
BassCode_Str[21] ="    " + "Game_Name = r'" +(Game_Name) +"'\n"


steamID3 = input(("steamID3\n>"))
BassCode_Str[26] ="    " + "steamID3 = " +(steamID3) +"\n"


Appid = input(("Appid\n>"))
BassCode_Str[30] ="    " + "Appid = " +(Appid) +"\n"


OS_32_or_64 = input(("OS_32_or_64\n>"))
BassCode_Str[33] ="    " + "OS_32_or_64 = " +(OS_32_or_64) +"\n"


NewGame = open("test_file.py", "w")

new_file_contents = "".join(BassCode_Str)

NewGame.write(new_file_contents)
NewGame.close()