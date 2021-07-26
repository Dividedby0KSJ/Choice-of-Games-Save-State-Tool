#This is the start file, the one the user clicks to start the program and does not tipicly get called
from runpy import run_module, run_path
import os
from time import sleep
#----------------------------------------------------- Debug -------------------------------------------------------

def debug():
    print("\nthis is the debug tool")
    print("0. Exit Progam")
    print("1. Exit debug tool")
    print("2. Hello TXT")
    print("3. Menu script")
    Choice = int(input("What code do you want to run? > "))
    if Choice == 0:
        exit()

    elif Choice == 1:
        print("Exiting tool, runing as normal")

    elif Choice == 2:
        run_module(mod_name='Hellotxt')
        debug()

    elif Choice == 3:
        run_module(mod_name='CogMenu')
        debug()
    else:
        print("invalid anser")
        debug()



#----------------------------------------------------- First Run -------------------------------------------------------

import glob
# All files ending with .txt
#print(glob.glob("First Run.txt")) 

if glob.glob("First Run.txt"):
    print("This has been run")

else:

    def FirstRun():

        FirstRun1 = open(".\First Run.txt", "w")
        FirstRun1.writelines("YES")
        FirstRun1.close

        print("\nFirst Run txt has been added\n")

        import subprocess
        subprocess.call([r'Dependencies.bat'])
 
        sleep(1)

        input("\n\ndependencys.bat is done, Making First run file. \n to run first start again del first run.txt\npress Enter")

    FirstRun()

#----------------------------------------------------- Code Start Code -------------------------------------------------------


def CodeStart():


    run_module(mod_name='Hellotxt')

    run_module(mod_name='CogMenu')

    run_module(mod_name='0CogSST-GoodByetxt')

    exit()

def NewGamePlus():

    NewGamePlus_Run = input(('Do You want to run "New Game Plus sript editer"? \n "Yes [Y] Or No [N] \n">'))

    if NewGamePlus_Run == "y" or NewGamePlus_Run == "Y":
        print("'Yes'")
        print("\n\nNew Game Plus sript editer opening\n\n")
        run_path(path_name='.NewGamePlus.py')
        NewGamePlus_PostCMD()

    elif NewGamePlus_Run == "n" or NewGamePlus_Run == "N":
        print("'No'")
        CodeStart()

    else:
        print("\n\nInvalid Answer!")
        NewGamePlus()

def NewGamePlus_PostCMD():
    NewGamePlus_Post = input(("\n\n\nDo you want to run CogSST? or just quit now?\n\nRun [R] Or Quit [Q] \n>"))
    
    if NewGamePlus_Post == "R" or NewGamePlus_Post == "r":
        print("Runing")

    elif NewGamePlus_Post == "Q" or NewGamePlus_Post == "q":
        print("Quiting")
        run_path(path_name='0CogSST-GoodByetxt.py')
        exit()
        
    else:
        print("\n\nInvalid Answer!")
        NewGamePlus_PostCMD()


#----------------------------------------------------- Code Start -------------------------------------------------------

# debug()

NewGamePlus()

CodeStart()