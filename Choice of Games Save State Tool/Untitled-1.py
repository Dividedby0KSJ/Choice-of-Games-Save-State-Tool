import os

Value69 = "ass"


TXTfile = Value69 + " fuck"

with open('Wait.txt', 'w+') as file:

    file.seek(0)

    file.writelines(TXTfile)

    file.seek(0)

    print(file.readlines())

    file.write("test")

    file.close()

os.remove("Wait.txt")