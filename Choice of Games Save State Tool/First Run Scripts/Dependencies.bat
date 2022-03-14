@echo off

type nul >".\First Run Scripts\Wait.txt"


:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------    



@REM The Admin Code above is from [ https://stackoverflow.com/questions/1894967/how-to-request-administrator-access-inside-a-batch-file ]
@REM Admin rights is needed to install Dependencies




python -m pip install --upgrade pip
pip install pypiwin32
pip install PySimpleGUI
pip install pyttsx3

DEL /s Wait.txt


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

@REM echo fuck my ass