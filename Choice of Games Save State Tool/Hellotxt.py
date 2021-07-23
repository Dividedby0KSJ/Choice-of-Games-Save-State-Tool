from time import sleep
import sys

#print(color.underline + 'Hello World !' + color.reset)

def A1():
    lines1 = ['\033[01m' "      Wellcom to Divided's",
            "Choice of Games Save state tool!" '\033[00m']

    for line in lines1:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.025)          # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)
A1()

sleep(0.5)

def A2():
    lines2 = ["You can't run this from the server if the",
            "drive path is difrent, as this code is not open",
            "to the publick you should know this \033[31m'Kieren'\033[0m >_>"]

    for line in lines2:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.0001)          # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)
A2()

#input()