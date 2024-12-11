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

sudo_pass = '5524Wildcats$$'
version = os.environ['DISTILLERY_VERSION']

sys.path.append(os.path.abspath("/home/justinackermann/StillPi/distillery/src"))
from display import *

# Start the distillery at power on
print("Starting DistilleryPi..")
print("Version: " + version)
print()

start_screen(version)
time.sleep(2)

# Check for updates
def git_updates():
    try:
        # Check the current branch
        branch_result = subprocess.run(
            ["git", "branch", "--show-current"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        current_branch = branch_result.stdout.strip()

        if branch_result.returncode != 0 or not current_branch:
            raise Exception("Error determining current branch:", branch_result.stderr.strip())

        print(f"Current branch: {current_branch}")

        # Fetch updates from the remote
        fetch_result = subprocess.run(
            ["git", "fetch"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if fetch_result.returncode != 0:
            raise Exception("Error fetching updates:", fetch_result.stderr.strip())

        print("Fetched updates from remote.")

        # Check if the local branch is behind the remote
        status_result = subprocess.run(
            ["git", "status", "-uno"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if "Your branch is behind" in status_result.stdout:
            print("Local branch is behind the remote. Pulling updates...")
            
            pull_result = subprocess.run(
                ["git", "pull"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            if pull_result.returncode == 0:
                print("Successfully pulled updates:")
                print(pull_result.stdout)
                return True
            else:
                raise Exception("Error pulling updates:", pull_result.stderr.strip())
        else:
            print("Local branch is up to date.")
            return False
        
    except Exception as e:
        raise e
    
# Check for updates
show_text_on_line(3, "Updating..", True)
did_update = git_updates()

# Reboot the Raspberry Pi
def reboot_raspberry_pi():
    try:
        # Ensure the script is run with sudo or root privileges
        # if os.geteuid() != 0:
        #     print("This script requires root privileges. Please run with sudo.")
        #     return
        
        # Use subprocess to call the reboot command
        print("Rebooting Raspberry Pi...")
        command = "reboot"
        os.system('echo %s|sudo -S %s' % (sudo_pass, command))
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to reboot: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if not did_update:
    print("No updates needed.")
    time.sleep(2)
    show_text_on_line(3, "No Updates Needed")
    time.sleep(2)
    show_text_on_line(3, "Starting program..")
    print("Starting distillery..")

else:
    print("Did update software:", did_update)
    print("Initiating reboot..")

    show_text_on_line(3, "Software Updated")
    time.sleep(2)
    show_text_on_line(3, "Rebooting..")
    time.sleep(2)
    
    reboot_raspberry_pi()
    
