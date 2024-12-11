#
# startup.py - This file contains the startup functionality for the distillery
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import sys
import os
import time
import subprocess

version = os.environ['DISTILLERY_VERSION']

sys.path.append(os.path.abspath("/home/justinackermann/StillPi/distillery"))
from display import *

# Start the distillery at power on
print("Starting DistilleryPi..")
print("Version: " + version)
print()

start_screen(version)
time.sleep(1.5)

# Check for updates
show_text_on_line(3, "Updating..", True)
    
# Pull the latest version from the git repository
try:
    command = "cd /home/justinackermann/StillPi && git pull"
    result = subprocess.check_output(command, shell=True)
    print(result.decode("utf-8"))
    time.sleep(2)
    sys.exit()

except subprocess.CalledProcessError as e:
    print(f"Error: {e.output.decode('utf-8')}")
    show_text_on_line(3, "Update Failed", True)
    time.sleep(2)
    sys.exit()