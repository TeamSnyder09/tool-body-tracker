@echo off
REM Quick launcher for Tool Body Tracker CLI
REM Sets Python path and runs the CLI with arguments

setlocal enabledelayedexpansion

set PYTHON_DIR=C:\Users\ksnyder\AppData\Local\Programs\Python\Python314
set PATH=!PYTHON_DIR!;!PATH!

REM Change to project directory
cd /d "C:\Users\ksnyder\OneDrive - Winbro Group Technologies Limited\Desktop\New project"

REM Run the CLI
python -m src.cli %*
