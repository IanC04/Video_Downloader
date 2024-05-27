@echo off & title %~nx0
cls

SET icon_url=https://raw.githubusercontent.com/IanC04/Video_Downloader/master/icon.ico
SET requirements_url=https://raw.githubusercontent.com/IanC04/Video_Downloader/master/requirements.txt
SET python_url=https://raw.githubusercontent.com/IanC04/Video_Downloader/master/YouTube.py

@REM REM Change directory to the script's directory
cd /D "%~dp0"
echo Current directory: %cd%

IF NOT EXIST .\icon.ico (
    echo icon.ico not found!
    curl -o icon.ico %icon_url%
)

IF NOT EXIST .\requirements.txt (
    echo requirements.txt not found!
    curl -o requirements.txt %requirements_url%
)

IF NOT EXIST .\YouTube.py (
    echo YouTube.py not found!
    curl -o YouTube.py %python_url%
)

IF NOT EXIST .\venv\Scripts\activate.bat (
    echo Creating virtual environment...
    python -m venv venv
    echo Installing dependencies...
    call .\venv\Scripts\activate.bat && pip install -r requirements.txt
) ELSE (
    echo Activating virtual environment...
    call .\venv\Scripts\activate.bat
)

start pythonw -m YouTube

EXIT /B