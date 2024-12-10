#! /bin/sh
export DISTILLERY_VERSION="0.0.2"

# Show the splash screen & do some initial setup
python3 startup.py

# Check for updates
cd /home/justinackermann/StillPi/distillery
if [[ `git status --porcelain` ]]; then
    echo "Changes detected in the distillery directory. Pulling latest changes..."
    git pull
fi