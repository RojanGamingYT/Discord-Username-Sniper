@echo off 
Title Download Modules...
python -m pip install -r requirements.txt
cls
Title Downloading Modules
echo python discord.py >> start.bat
start start.bat