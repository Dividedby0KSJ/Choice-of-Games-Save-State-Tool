from runpy import run_module, run_path
import glob
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Print

sg.theme('Black')   # Add a touch of color

def Gamelist():
    for n, each in enumerate(glob.glob('CogSST-*.py'), start=1):
        print(n, each)

# Gamelist = for n, each in enumerate(glob.glob('CogSST-*.py'), start=1)

CogSSTFile = 'NA'

CogMenuLayout = [
    [sg.Input(), sg.FileBrowse('GogSST File', file_types=[("Python files", "CogSST-*.py")])],
    [sg.Button(button_text="Open"), sg.Button(button_text="Cancel")],
    # [sg.Text('Ass')],
]

CogMenuWindow = sg.Window('Game Manager', CogMenuLayout)

while True:
    event, values = CogMenuWindow.read()

    if event == sg.WIN_CLOSED:
        exit()
    if event is None or event == 'Cancel':
        break

    if event == 'Open':
        # print("Open Clicked")
        CogSSTFile = values['GogSST File'] or 'NA'
        
        if CogSSTFile == 'NA':
            print('Error! No Path Found!')
        
        else:
            print("File Path: ",CogSSTFile)
            CogMenuWindow.close()
            run_path(path_name=(CogSSTFile))
            break

CogMenuWindow.close()