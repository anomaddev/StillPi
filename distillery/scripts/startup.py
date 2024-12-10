#
# startup.py - This file contains the startup functionality for the distillery
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

import sys
import os

version = os.environ['DISTILLERY_VERSION']
print("Starting DistilleryPi..")
print("Version: " + version)

sys.path.append(os.path.abspath("/home/justinackermann/StillPi/distillery"))
from display import *

start_screen(version)