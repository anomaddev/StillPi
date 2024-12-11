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

import git

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

repo = git.Repo("/home/justinackermann/StillPi")
repo.remotes.origin.pull()

