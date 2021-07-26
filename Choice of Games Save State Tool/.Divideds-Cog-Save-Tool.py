#This is the start file, the one the user clicks to start the program and does not tipicly get called
from runpy import run_module
import os
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

        FirstRun1 = open("First Run.txt", "w")
        FirstRun1.writelines("YES")
        FirstRun1.close

        print("First Run txt has been added")

    FirstRun()

#----------------------------------------------------- Code Start -------------------------------------------------------

# debug()

def CodeStart():


    run_module(mod_name='Hellotxt')

    run_module(mod_name='CogMenu')

    run_module(mod_name='0CogSST-GoodByetxt')

    exit()

CodeStart()