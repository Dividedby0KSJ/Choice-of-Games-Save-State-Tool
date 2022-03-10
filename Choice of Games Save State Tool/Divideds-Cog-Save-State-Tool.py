import glob, os, subprocess
from time import sleep

Sys32 = os.getcwd()
if Sys32 == "C:\WINDOWS\system32":
    print ("!!! For some reason, the program has started in System32! !!! \nThe program can not run in this directory. please check the help file for how to fix")
    input("Press enter to exit...")
    exit()


# Check if If in the github directory or in the Release directory
if os.path.exists(r"./Choice of Games Save State Tool") :
    # Change the current working Directory    
    os.chdir(r"./Choice of Games Save State Tool")
else:
    print("Can't change the Current Working Directory\nOr Already in correct directory.")

#----------------------------------------------------- Wait.txt Clean -------------------------------------------------------

if glob.glob("Wait.txt"):
    print("This shouldint be here!")
    os.remove("Wait.txt")

if glob.glob(r'.\First Run Scripts\Wait.txt'):
    print("This shouldint be here!")
    os.remove("Wait.txt")

#----------------------------------------------------- First Run -------------------------------------------------------

# Checks if the code has been run before, if not it will install the dependencys.
if glob.glob(r'.\First Run Scripts\First Run.txt'):
    print("First Run.txt Is in dir, continuing")

else:

    def FirstRun():
     
        subprocess.Popen([r".\First Run Scripts\First Run TTS.py"], shell=True, creationflags=subprocess.SW_HIDE)

        subprocess.Popen([r'.\First Run Scripts\Dependencies.bat'], shell=True)

        sleep(2) #this is to ensure that the .bat file makes the Wait.txt file.

        # This it a infinite loop that keeps waiting until the Wait.txt file is deleted (not found)
        def WaitFirstSetup():

            if glob.glob(r'.\First Run Scripts\Wait.txt'):
                sleep(0.5)
                WaitFirstSetup()
            else:
                print("Wait.txt gone, proceeding")
        WaitFirstSetup()

        # Add's a file in the <\First Run Scripts> Dir to tell the program that the dependencys are instaled
        FirstRun1 = open(r'.\First Run Scripts\First Run.txt', "x")
        FirstRun1.writelines("YES")
        FirstRun1.close

        print("\nFirst Run txt has been added\n")

    FirstRun()

#----------------------------------------------------- Code Start Code -------------------------------------------------------

from runpy import run_module, run_path
import PySimpleGUI as sg
import sys, pyttsx3


exit()

if glob.glob("Wait.txt"):
    print("This shouldint be here!")
    os.remove("Wait.txt")


# run_path(path_name='Hellotxt.py')


# This prevents the next sript from runing if the Wait.txt is present
while True:
    sleep(2)
    if glob.glob("Wait.txt"):
        sleep(0.1)
    else:
        break


run_path(path_name='.NewGamePlus.py')


# This prevents the next sript from runing if the Wait.txt is present
while True:
    sleep(2)
    if glob.glob("Wait.txt"):
        sleep(0.1)
    else:
        break


run_path(path_name='CogMenu.py')