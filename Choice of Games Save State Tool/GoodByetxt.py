from time import sleep
import sys

#print(color.underline + 'Hello World !' + color.reset)


def A1():
    lines1 = ["Good Bye!"]

    for line in lines1:          # for each line of text (or each message)
        for c in line:          # for each character in each line
            print(c, end='')    # print a single character, and keep the cursor there.
            sys.stdout.flush()  # flush the buffer
            sleep(0.025)          # wait a little to make the effect look good.
        print('')               # line break (optional, could also be part of the message)
A1()

sleep(1)

exit()
#input()