#!/bin/sh
echo "Ziehe Änderungen aus dem Github-Repo"
git pull
echo "Starte Bot..."
nohup python3 seyffbot.py
echo "Beende Bot."