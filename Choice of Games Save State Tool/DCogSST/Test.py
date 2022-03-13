import PySimpleGUI as sg
from time import sleep
import os, subprocess, glob, platform

# System 32 Dir Check
Sys32 = os.getcwd()
if Sys32 == "C:\WINDOWS\system32":
    print ("!!! For some reason, the program has started in System32! !!! \nThe program can not run in this directory. please check the help file for how to fix")
    input("Press enter to exit...")
    exit()

# Check if If in the github directory or in the Release directory
if os.path.exists(r"./Choice of Games Save State Tool") :
    # Change the current working Directory    
    os.chdir(r"./Choice of Games Save State Tool")
# else:
#     print("Can't change the Current Working Directory\nOr Already in correct directory.")

sg.theme('Black')   # PySimpleGUI Theme


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Null ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

subprocess.Popen([r".\TTS\NewGame\BitOsError.py"], shell=True, creationflags=subprocess.SW_HIDE)

print("\nThe program cannot detect the os bit!")
print("Make sure that you are running this program in windows!")
print("If you are, and want to force the program to continue!")
print("Make a .txt file in the Variables directory with the architecturey you are running in!")
print("Example: Bit32.txt or Bit64.txt!")

input("Press enter to Exit")
exit()
