#! /bin/sh
export DISTILLERY_VERSION="0.0.2"

# Show the splash screen & do some initial setup
python3 startup.py

# Check for updates
echo "Checking for updates..."
python3 -c'import startup; startup.isUpdating()'

cd /home/justinackermann/StillPi/distillery
git remote update && git status && git pull origin main

