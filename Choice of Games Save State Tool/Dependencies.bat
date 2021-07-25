python -m pip install --upgrade pip
pip install pyttsx3==2.71
pip install pypiwin32


@echo off
echo .
echo .
echo .
echo Do you want to Del This file now that you have instaled the dependencies?[Y/N]
choice /c YN
if %errorlevel%==1 goto yes
if %errorlevel%==2 goto no

:yes
echo yes
goto :Del

:no
echo no
exit

:Del
goto 2>nul & del "%~f0"