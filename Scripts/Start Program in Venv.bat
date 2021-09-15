@echo off
title Script: Start Program in Venv
cls
set /p id=Enter name of script to start (with extension, for example: esp_4_postman_request.py): 
echo Starting python venv...
cmd /c "%~dp0..\.venv\Scripts\activate.bat & echo Starting %id%...& echo ---------- START ESP OUTPUT ---------- & py ..\%id% & deactivate"
echo ----------- END ESP OUTPUT -----------
echo Finished python venv.
pause
