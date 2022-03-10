import glob, os, subprocess
from time import sleep
from runpy import run_module, run_path
import PySimpleGUI as sg
import sys, pyttsx3

#----------------------------------------------------- Code Start Code -------------------------------------------------------

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