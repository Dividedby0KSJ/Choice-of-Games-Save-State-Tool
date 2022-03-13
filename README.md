# Choice-of-Games-Save-State-Tool
![Cog Save State Tool logo](https://i.imgur.com/3TJANMm.png)

## About the Program

This is a python program to save and load at any point in any Choice of Games Game

This is the first big python program that i have ever made so bug will be plentiful!  

&nbsp;

If you Play any Choice of Games, you will know there is no save slots like in other games, and in Cog Games 1 Choice can lead to a good ending or bad ending... or death.

And as my may or may not know Cog games are bassed on Choose Your Own Adventure Books. In thoes books you can just go back a few pages if you make a wrong choice or die.
This is the point of this tool.

&nbsp;

# How to use

This code has gone through (and is currently being remade) major code changes!
As far as i know, the latest comand line release is the most stable. [THIS IS THE CMD RELEASE]
In my brake I have been learning and now have better practecs.
pleas be patent.


## #01 Python
First things first are, you need python 3, I used python 3.9.4 to make this program but any python 3 and up **_Should_** work.

[Python Download](https://www.python.org/downloads/) <--- This link will take you to the Python download page and will download the most recent version of python.

&nbsp;

# After this point is not needed to know
After this point is just how to use if you need more info than the program alredy givs you. so if you have done step #1 than all you need to do is just run `.Divideds-Cog-Save-State-Tool.py`

# &nbsp;

## #02 Python Dependencies
I have added a bat file that once python is installed it will updated pip _(Python's module downloader)_, download and install the needed modules.

You Can ether run this by the .bat file or by runing the main file for the first time.

&nbsp;

## #03 Game pacific scripts
By default, there will be no game scripts, but there is `.NewGamePlus.py` witch will ask for 5 variables and make a `.py` file.

The Script will ask for a few things, however I made it very easy to work with and all you the user needs to do is fill out 5 variables that are easy to understand.

&nbsp;

### `RootDir = r"C:/Users/UserName/Saved Games/CogSST"`

`RootDir` is the Dir where the save states will be added, the directory that is there is just a demo of where you can put save games.

Just type where you want your saves to go.

&nbsp;

### `Game_Name = r"Game Name"`

You need the name of the game or what you want the code to call the game.

!YOU CANNOT USE! THE FOLLOWING RESERVED CHARACTERS IN THE GAME NAME:

`< (less than)`

`> (greater than)`

`: (colon)`

`" (double quote)`

`/ (forward slash)`

`\ (backslash)`

`| (vertical bar or pipe)`

`? (question mark)`

`* (asterisk)`

&nbsp;

### `steamID3 = 123456789`

This is your steam ID 3, for example yous might look like [U:1:123456789] you need the last set of numbers, not the 'U:1:'
or the [], so take out the [U:1:] and leave the other numbers and put them in the steamID3 tag.

Use this website to get your steamID3: https://steamid.io or https://steamidfinder.com

Remeber! DO NOT INCLUDE THE '[]' OR 'U:1:

&nbsp;

### `Appid = 123456789`

The Cog App ID of the game you want to manage.

Check this link for the games id's for all of Cog games: https://steamdb.info/search/?a=app_keynames&type=-1&keyname=23&operator=3&keyvalue=Choice+of+Games

&nbsp;

### `OS_32_or_64 = 0`

Put here whether your os is 32bit or 64bit, put either 32 or 64 as just numbers, leave out the "bit".

**ONLY THESE EXAMPLES WILL WORK:**

`32` or `64`

If you dont know, open 'System Information' and look under 'System type' if it says x64-based than you are 64.

&nbsp;

# About me

I dont know how to use markdown or git or github but ill laern the ladder and bring to you my program!

My spelling to horible FYI.

Feedback is greatly appreciated! (Unless its about my spelling)
