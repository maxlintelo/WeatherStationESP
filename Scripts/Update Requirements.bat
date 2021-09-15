@echo off
title Script: Update Requirements
cls
echo Starting python venv...
cmd /c "%~dp0..\.venv\Scripts\activate.bat & echo Updating requirements... & echo ---------- START PIP OUTPUT ---------- & pip install -r ..\requirements.txt & deactivate"
echo ----------- END PIP OUTPUT -----------
echo Finished python venv.
pause
