import os
import shutil

ModsFolder = "P:/AppData/Roaming/.minecraft/mods"
onePOINTfourteenPOINTfourMODSFOLDER = "K:/Games/MultiMC/mods/1.14.4 forge"
onePOINTtwelvePOINTtwoMODSFOLDER = "K:/Games/MultiMC/mods/1.12.2 forge"
onePOINTfourteenPOINTfourMODSLightFOLDER = "K:/Games/MultiMC/mods/1.14.4 Light forge"
onePOINTfourteenPOINTfourMODSActuallyLightFOLDER = "K:/Games/MultiMC/mods/1.14.4 Actually Light forge"
onePOINTsixteenPOINToneFORGEFOLDER = "K:/Games/MultiMC/mods/1.16.1 Forge"
onePOINTsixteenPOINTfourFORGEFOLDER = "K:/Games/MultiMC/mods/1.16.4 Forge"


def Menu():
    print("\n\n1. Vanilla")
    print("2. 1.14.4")
    print("3. 1.14.4 Light")
    print("4. 1.14.4 Actually Light")
    print("5. 1.12.2")
    print("6. 1.16.1 Forge")
    print("7. 1.16.4 Forge")
    print("0. End")

    Choice = int(input("Enter Choice: "))
    if Choice == 0:
        exit

    elif Choice == 1:
        Vanilla()

    elif Choice == 2:
        onePOINTfourteenPOINTfour()

    elif Choice == 3:
        onePOINTfourteenPOINTfourLight()

    elif Choice == 4:
        onePOINTfourteenPOINTfourActuallyLight()

    elif Choice == 5:
        onePOINTtwelvePOINTtwo()

    elif Choice == 6:
        onePOINTsixteenPOINToneFORGE()

    elif Choice == 7:
        onePOINTsixteenPOINTfourFORGE()

    else:
        print("\n\nU wot m8? \nPlz input right answer m8!\n\n")
        Menu()


def Vanilla():
    print("\nDeleting Contents of mods folder\n")

    for filename in os.listdir(ModsFolder):
        file_path = os.path.join(ModsFolder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    anykey = input(
        "Command sent successfully please wait a few seconds then\nPress the 'Enter' key to go back to the menu")
    Menu()


def onePOINTfourteenPOINTfour():
    print("Copying 1.14.4 Mods to 'Mods' Folder\nPlease wait")
    shutil.copytree(src=onePOINTfourteenPOINTfourMODSFOLDER,
                    dst=ModsFolder, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Menu()


def onePOINTfourteenPOINTfourLight():
    print("Copying 1.14.4 Light Mods to 'Mods' Folder\nPlease wait")
    shutil.copytree(src=onePOINTfourteenPOINTfourMODSLightFOLDER,
                    dst=ModsFolder, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Menu()


def onePOINTfourteenPOINTfourActuallyLight():
    print("Copying 1.14.4 Actually Light Mods to 'Mods' Folder\nPlease wait")
    shutil.copytree(src=onePOINTfourteenPOINTfourMODSActuallyLightFOLDER,
                    dst=ModsFolder, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Menu()


def onePOINTtwelvePOINTtwo():
    print("Copying 1.12.2 Mods to 'Mods' Folder\nPlease wait")
    shutil.copytree(src=onePOINTtwelvePOINTtwoMODSFOLDER,
                    dst=ModsFolder, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Menu()

def onePOINTsixteenPOINToneFORGE():
    print("Copying 1.16.1 Mods to 'Mods' Folder\nPlease wait")
    shutil.copytree(src=onePOINTsixteenPOINToneFORGEFOLDER,
                    dst=ModsFolder, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Menu()

def onePOINTsixteenPOINTfourFORGE():
    print("Copying 1.16.4 Mods to 'Mods' Folder\nPlease wait")
    shutil.copytree(src=onePOINTsixteenPOINTfourFORGEFOLDER,
                    dst=ModsFolder, dirs_exist_ok=True)
    anykey = input("Press the 'Enter' key to go back to the menu")
    Menu()


def CTT():
    print("")

    print("Done")
    anykey = input("Press the 'Enter' key to go back to the menu")
    Menu()

# ignore=shutil.ignore_patterns(".*")


def Logo():
    print('''
██╗  ██╗██╗███████╗██████╗ ███████╗███╗   ██╗███████╗                    
██║ ██╔╝██║██╔════╝██╔══██╗██╔════╝████╗  ██║██╔════╝                    
█████╔╝ ██║█████╗  ██████╔╝█████╗  ██╔██╗ ██║███████╗                    
██╔═██╗ ██║██╔══╝  ██╔══██╗██╔══╝  ██║╚██╗██║╚════██║                    
██║  ██╗██║███████╗██║  ██║███████╗██║ ╚████║███████║                    
╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝                    
                                                                         
███╗   ███╗██╗███╗   ██╗███████╗ ██████╗██████╗  █████╗ ███████╗████████╗
████╗ ████║██║████╗  ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
██╔████╔██║██║██╔██╗ ██║█████╗  ██║     ██████╔╝███████║█████╗     ██║   
██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║     ██╔══██╗██╔══██║██╔══╝     ██║   
██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╗██║  ██║██║  ██║██║        ██║   
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝   
                                                                         
███╗   ███╗ ██████╗ ██████╗         ██╗   ██╗███████╗██████╗             
████╗ ████║██╔═══██╗██╔══██╗        ██║   ██║██╔════╝██╔══██╗            
██╔████╔██║██║   ██║██║  ██║        ██║   ██║█████╗  ██████╔╝            
██║╚██╔╝██║██║   ██║██║  ██║        ╚██╗ ██╔╝██╔══╝  ██╔══██╗            
██║ ╚═╝ ██║╚██████╔╝██████╔╝         ╚████╔╝ ███████╗██║  ██║            
╚═╝     ╚═╝ ╚═════╝ ╚═════╝           ╚═══╝  ╚══════╝╚═╝  ╚═╝            
                                                                         
██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗                         
██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗                        
██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝                        
██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗                        
███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║                        
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝                        
                                                                         
''')


Logo()

print("\n\nWelcome Kieren. \nWitch Ver of Mincraft wold you like to import you mods into?\n")

Menu()

# Move a file by renaming it's path
# os.rename('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')

# Move a file from the directory d1 to d2

# shutil.move('/Users/billy/d1/xfile.txt', '/Users/billy/d2/xfile.txt')1
