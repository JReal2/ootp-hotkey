@echo off
title OOTP Hotkey Runner (Conda Env: ootp)

REM Change directory to the script's location
cd /d "%~dp0"

echo Starting OOTP Hotkey script in 'ootp' conda environment...
echo If this fails, please ensure you have created the 'ootp' conda environment and installed the requirements as per the README.md file.
echo.

REM Run the python script within the 'ootp' conda environment
start /b "" conda run -n ootp python ootp_hotkey.py

echo The script is now running in the background.

pause
