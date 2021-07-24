from runpy import run_module

#----------------------------------------------------- Menu -------------------------------------------------------

def Game_Menu():
    print("\n\n0. Exit")
    print("1. Avatar of the Wolf")

    Choice = int(input("Witch Game Do You Want To Mange > "))
    if Choice == 0:
        run_module(mod_name='GoodByetxt')

    elif Choice == 1:
        run_module(mod_name='Avatar_Of_The_Wolf')
   
    else:
        print("\n\nInvalid Answer\n\n")
        Game_Menu()

#----------------------------------------------------- Code Start -------------------------------------------------------

Game_Menu()
