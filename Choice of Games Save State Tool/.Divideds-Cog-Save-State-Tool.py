from runpy import run_module, run_path
from time import sleep
import PySimpleGUI as sg
import os, sys, glob




#----------------------------------------------------- First Run -------------------------------------------------------

if glob.glob("First Run.txt"):
    print("First Run.txt exists. Continuing to Main Menu")

else:

    def FirstRun():

        YesNoButtonLayout = [

            [sg.Button(button_text="Yes", button_color="Green"), sg.Button(button_text="No", button_color="Red")]
            
            ]

        FirstRunWindowLayout = [

            [sg.Text('First Run.txt is not detected!')],
            [sg.Text('Do you want to run the first run program to install dependencies?')],
            [sg.Image(filename='./Loading.gif')],
            [sg.Column(YesNoButtonLayout, key='__Yes_No_Button_Layout__', visible=True)]

        ]

        FirstRunWindow = sg.Window('First Run', FirstRunWindowLayout)
        while True:
            event, values = FirstRunWindow.read()
            if event == sg.WIN_CLOSED:
                sys.exit()
            if event == 'No':
                break
            if event == 'Yes':
                FirstRunWindow['__Yes_No_Button_Layout__'].update(visible=False)



                # FirstRun1 = open(".\First Run.txt", "w")
                # FirstRun1.writelines("This is the first file used to see if the program has been run before.")
                # FirstRun1.close

                # print("\nFirst Run txt has been added\n")

                # import subprocess
                # subprocess.call([r'Dependencies.bat'])
        
                # sleep(1)

                print("\n\ndependencys.bat is done, Making First run file. \n to run first start again del first run.txt\npress Enter")

                # break
        FirstRunWindow.close()

    FirstRun()

print("ass")
#----------------------------------------------------- Code Start Code -------------------------------------------------------
