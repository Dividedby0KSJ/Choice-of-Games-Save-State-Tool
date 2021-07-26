from time import sleep
import sys, subprocess

#print(color.underline + 'Hello World !' + color.reset)

#runs the TTS engin in another termainal to prevent it from interupting the text scrole
subprocess.Popen(['TTS Lines\HelloTTS.py'], shell=True, creationflags=subprocess.SW_HIDE)

def A1():
    lines1 = ["\n\n           \033[95mWellcom to Divided's",
            "     Choice of Games Save state tool!\033[00m"]

    for line in lines1:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.0315)          # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)
A1()

sleep(0.)

def A2():
    lines2 = ["        Made by 'Kieren St James'",
            "             Love you all <3",
            "\033[31m                 v.0.7.1\033[0m"]

    for line in lines2:         # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.001)      # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)
A2()

#anykey = input()