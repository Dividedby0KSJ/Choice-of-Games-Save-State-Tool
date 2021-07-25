# The file to read from
BassCode_File = open("Hellotxt.py")

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


BassCode_Str[3] ="\n#Null my dick\n"


NewGame = open("test_file.py", "w")

new_file_contents = "".join(BassCode_Str)

NewGame.write(new_file_contents)
NewGame.close()