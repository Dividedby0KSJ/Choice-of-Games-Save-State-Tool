#This is the start file, the one the user clicks to start the program and does not tipicly get called
from runpy import run_module
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

# debug()

#----------------------------------------------------- Code Start -------------------------------------------------------
import Hellotxt

run_module(mod_name='CogMenu')

run_module(mod_name='GoodByetxt')

exit()