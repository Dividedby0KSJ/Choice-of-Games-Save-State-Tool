from runpy import run_module

#----------------------------------------------------- Menu -------------------------------------------------------

def Game_Menu():
    print("\n\n0. Exit")
    print("1. Choice of the Dragon")
    print("2. Fox Spirit")
    print("3. Werewolves Haven Rising")
    print("4. Wolf")

    Choice = int(input("Witch Game Do You Want To Mange > "))
    if Choice == 0:
        exit

    elif Choice == 1:
        run_module(mod_name='CoT_Dragon_Menu')

    elif Choice == 2:
        run_module(mod_name='Fox_Spirit_Menu')

    elif Choice == 3:
        run_module(mod_name='Werewolves_Haven_Rising_Menu')

    elif Choice == 4:
        run_module(mod_name='Avatar_Of_The_Wolf')
   
    else:
        print("\n\nInvalid Answer\n\n")
        Game_Menu()

#----------------------------------------------------- Code Start -------------------------------------------------------

Game_Menu()

exit()