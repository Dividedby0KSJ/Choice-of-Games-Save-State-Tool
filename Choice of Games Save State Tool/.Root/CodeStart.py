import glob, os, subprocess
from time import sleep
from runpy import run_module, run_path
import PySimpleGUI as sg
import sys, pyttsx3


#----------------------------------------------------- OS Dir Check -------------------------------------------------------

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


#----------------------------------------------------- Code Start Code -------------------------------------------------------


run_path(path_name='.\GUI\HellotxtGUI.py')


# This prevents the next sript from runing if the Wait.txt is present
while True:
    sleep(2)
    if glob.glob("Wait.txt"):
        sleep(0.1)
    else:
        break


# run_path(path_name='.NewGamePlus.py')


# This prevents the next sript from runing if the Wait.txt is present
while True:
    sleep(2)
    if glob.glob("Wait.txt"):
        sleep(0.1)
    else:
        break


# run_path(path_name='CogMenu.py')