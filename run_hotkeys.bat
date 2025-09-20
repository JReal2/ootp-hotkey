@echo off
title OOTP Hotkey Runner

REM Change directory to the script's location
cd /d "%~dp0"

echo Checking for required Python libraries from requirements.txt...
pip install -r requirements.txt

echo.
echo Starting OOTP Hotkey script...
echo.

REM Run the python script using the 'python' command, assuming it's in the PATH.
REM If this fails, the user may need to edit this line to point to their python.exe
start /b "" python ootp_hotkey.py

echo The script is now running in the background.
echo You can close this window.
echo.
echo Hotkeys:
echo   F8: Auto-play until tomorrow
echo   F9: Save game
echo   F12: Stop the script
echo.
pause
