import PySimpleGUI as sg

# sg.Window(title="Hello World", layout=[[]], margins=(300,100)).read()
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.Input(do_not_clear=False, size=(5),)],
            [sg.Button('Ok', button_type=1), sg.Button('Cancel')],
            [sg.Button('AssFuck')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'AssFuck':
        print("you fucked my ass!")
    if event == 'Ok':
        print('You entered ', values[0])

window.close()