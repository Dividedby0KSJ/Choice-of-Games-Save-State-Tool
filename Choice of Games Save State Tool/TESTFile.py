import os
import PySimpleGUI as sg

Layout = [
    [sg.Input(focus=True, key='AssFuck'), sg.FolderBrowse('Folder')],
    [sg.Text("Game Name >", justification='Right') , sg.Button(button_text='Submit', button_color='Green')],
]

Window = sg.Window("RootDir", Layout, font=('',14), element_justification='Center')

while True:
    event, values = Window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        exit()
    if event == 'Submit':
        InputValue = values['AssFuck'] or 'ERROR'
        # break
        print (InputValue)
    
Window.close

DirWithBackSlash = r"C:\Users\Divided_By_Zero\Saved Games\CogSST"