#
# startup.py - This file contains the startup functionality for the distillery
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
#

from distillery.display import start_screen
import os

version = os.environ['DISTILLERY_VERSION']
print("Starting DistilleryPi..")
print("Version: " + version)

start_screen(version)