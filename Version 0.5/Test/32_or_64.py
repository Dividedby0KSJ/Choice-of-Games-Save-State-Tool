#----------------------------------------------------- Bit --------------------------------------------------
from time import sleep
import glob, platform
# All files ending with .txt
#print(glob.glob("Bit.txt")) 

if glob.glob("Bit64.txt") or glob.glob("Bit32.txt"):
    print("This has already been ran")

else:

    OSbit = platform.machine().endswith('64')

    # print(OSbit)

#---------------------------------------------------------------- Bit Prosesing -------------------------------------------------------
    def Bit64():

        Bit1 = open(".\Bit64.txt", "x")
        Bit1.writelines("64Bit OS, the beast one!")
        Bit1.close

    def Bit32():

        Bit2 = open(".\Variables\Bit32.txt", "w")
        Bit2.writelines("32Bit OS or x86")
        Bit2.close
#----------------------------------------------------- Bit Detections ---------------------------------------------------------------


    if OSbit == True:
        print("this is 64bit")
        Bit64()

    elif OSbit == False:
        print("this is not 64bit")
        Bit32()

    else:
        print("this is not 64bit or 32bit \n ERROR: Unknown OSbit")