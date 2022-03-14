from runpy import run_path
import glob, os
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Print



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


sg.theme('Black')   # Add a touch of color

def Gamelist():
    for n, each in enumerate(glob.glob('DCogSST-*.py'), start=1):
        print(n, each)

# Gamelist = for n, each in enumerate(glob.glob('DCogSST-*.py'), start=1)

DCogSSTFile = 'NA'

CogMenuLayout = [
    [sg.Text("Use the 'DCogSST File' Button to open the game save state manager", justification='Center', font=('Helvitica',12))],
    [sg.Input(size=(55), key="DCogSST File Input"), sg.Push(), sg.FileBrowse('DCogSST File', target="DCogSST File Input", file_types=[("Python files", "DCogSST-*.py")])],
    [sg.Button(button_text="Open"), sg.Button(button_text="Cancel", button_color = 'red'), sg.Push(), sg.Button(button_text="New Cog Game", button_color = '#33ff63',)],
    # [sg.Text('Ass')],
]

CogMenuWindow = sg.Window('Game Manager', CogMenuLayout)

while True:
    event, values = CogMenuWindow.read()

    # The exit buttons and close buttons
    if event == sg.WIN_CLOSED:
        exit()
    if event is None or event == 'Cancel':
        break

    # The open button that checks the file path for the DCogSST-*.py File and opens it.
    if event == 'Open':
        # print("Open Clicked")
        DCogSSTFile = values['DCogSST File'] or 'NA'
        
        if DCogSSTFile == 'NA':
            print('Error! No Path Found!')
        
        else:
            print("File Path: ",DCogSSTFile)
            CogMenuWindow.close()
            run_path(path_name=(DCogSSTFile))
            break

    if event == 'New Cog Game':
        CogMenuWindow.close()
        run_path(path_name='.\DCogSST\.NewGame.py')

CogMenuWindow.close()