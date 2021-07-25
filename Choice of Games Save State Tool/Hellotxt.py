from time import sleep
import sys, os, subprocess

#print(color.underline + 'Hello World !' + color.reset)

#runs the TTS engin in another termainal to prevent it from interupting the text scrole
#os.startfile('HelloTTS.py') #('HelloTTS.py')



def A1():
    lines1 = ['\033[95m' "           Wellcom to Divided's",
            "     Choice of Games Save state tool!" '\033[00m']

    for line in lines1:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.02)          # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)
A1()

sleep(0.)

def A2():
    lines2 = ["                  Hello",
            "                  World!",
            "\033[31m             pee pee poo poo\033[0m"]

    for line in lines2:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.001)          # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)
A2()

#anykey = input()