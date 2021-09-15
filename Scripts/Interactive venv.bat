@echo off
title Script: Activate venv
cls
echo Starting python venv...
cmd /k "%~dp0..\.venv\Scripts\activate.bat"
echo Finished python venv.
pause
