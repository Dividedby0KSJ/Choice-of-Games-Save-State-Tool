from runpy import run_module, run_path
import glob

#----------------------------------------------------- Menu -------------------------------------------------------

# def Game_Menu():
#     print("\n\n0. Exit")
#     print("1. Avatar of the Wolf")

#     Choice = int(input("Witch Game Do You Want To Mange > "))
#     if Choice == 0:
#         run_module(mod_name='0CogSST-GoodByetxt')

#     elif Choice == 1:
#         run_module(mod_name='Avatar_Of_The_Wolf')
   
#     else:
#         print("\n\nInvalid Answer\n\n")
#         Game_Menu()

def Game_MenuV2():
    # print("Dev Game_MenuV2")
    print('0 Exit')
    for n, each in enumerate(glob.glob('CogSST-*.py'), start=1):
        print(n, each)


    # print('0. Is Exit Program')

    # print(pyfile, each)    
    ask = int(input("Witch Game Do You Want To Mange > "))

    CogSST_File = glob.glob('*CogSST-*.py')[ask]

    # print(CogSST_File)

    run_path(path_name=(CogSST_File))

    # for n, each in enumerate(os.listdir()):
    #     print(n, each)

    # ask = int(input("Number? > "))
    # 
    # Restore_Folder_Name = os.listdir()[ask]


#----------------------------------------------------- Code Start -------------------------------------------------------

# Game_Menu()

Game_MenuV2()