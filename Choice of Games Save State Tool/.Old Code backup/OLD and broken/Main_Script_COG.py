import os

#this is the Menu... duhh
def Menu():
    print("\n\n0. Exit")
    print("1. Choice of the Dragon")
    print("2. Fox Spirit")

    Choice = int(input("Witch Game Do You Want To Mange > "))
    if Choice == 0:
        exit

    elif Choice == 1:
        exec(open('Choice_of_the_Dragon.py').read())

    elif Choice == 2:
        os.system('Fox_Spirit.py')
   
    else:
        print("\n\nInvalid Answer\n\n")
        Menu()


#All the def for stuff in the Menu

def Test():
    import Folder_Maker_defult



#-------------------------------------------------- the code starts here --------------------------------------------------


Menu()