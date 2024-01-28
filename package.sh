#! /bin/sh

# pip3 freeze > requirements.txt
pyinstaller -w -F App.py Speaker.py Teacher.py
