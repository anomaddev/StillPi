#
# startup.py - This file contains the startup functionality for the distillery
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import sys
import os
import time

version = os.environ['DISTILLERY_VERSION']
print("Starting DistilleryPi..")
print("Version: " + version)
print()

sys.path.append(os.path.abspath("/home/justinackermann/StillPi/distillery"))
from display import *

start_screen(version)
time.sleep(1.5)

def isUpdating():
    show_text_on_line(3, "Updating..", True)
    