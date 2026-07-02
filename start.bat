@echo off
title WordGuesser_PY
cd /d "%~dp0"

python main.py

if errorlevel 1 (
    echo.
    echo ERROR: can't start game. Check if Python is installed and in PATH.
    pause
)