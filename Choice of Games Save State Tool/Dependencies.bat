python -m pip install --upgrade pip
pip install pyttsx3==2.71
pip install pypiwin32
pip install PySimpleGUI


@REM @echo off
@REM echo .
@REM echo .
@REM echo .
@REM echo Do you want to Del This file now that you have instaled the dependencies?[Y/N]
@REM choice /c YN
@REM if %errorlevel%==1 goto yes
@REM if %errorlevel%==2 goto no

@REM :yes
@REM echo yes
@REM goto :Del

@REM :no
@REM echo no
@REM exit

@REM :Del
@REM goto 2>nul & del "%~f0"