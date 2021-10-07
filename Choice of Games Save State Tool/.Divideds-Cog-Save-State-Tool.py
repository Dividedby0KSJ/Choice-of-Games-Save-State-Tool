from runpy import run_module, run_path
from time import sleep
import PySimpleGUI as sg
import os, sys, glob, pyttsx3


#----------------------------------------------------- First Run -------------------------------------------------------

# All files ending with .txt
#print(glob.glob("First Run.txt")) 

if glob.glob("First Run.txt"):
    print("This has been run")

else:

    def FirstRun():

        import subprocess
        subprocess.call([r'Dependencies.bat'])
 
        sleep(1)

        FirstRun1 = open(".\First Run.txt", "w")
        FirstRun1.writelines("YES")
        FirstRun1.close

        print("\nFirst Run txt has been added\n")

        input("\n\ndependencys.bat is done, Making First run file. \n to run first start again del first run.txt\npress Enter")

    FirstRun()

#----------------------------------------------------- Code Start Code -------------------------------------------------------

if glob.glob("Wait.txt"):
    print("This shouldint be here!")
    os.remove("Wait.txt")

run_path(path_name='Hellotxt.py')

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