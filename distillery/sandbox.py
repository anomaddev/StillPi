#
# sandbox.py - This file contains sandbox functionality and testing
# Date Created: 12/01/2024
# Author: Justin Ackermann
#
# Description: This file contains experimental code and testing
#
#

import subprocess

def check_and_update_remote():
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
            print("Error determining current branch:", branch_result.stderr.strip())
            return

        print(f"Current branch: {current_branch}")

        # Fetch updates from the remote
        fetch_result = subprocess.run(
            ["git", "fetch"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if fetch_result.returncode != 0:
            print("Error fetching updates:", fetch_result.stderr.strip())
            return

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
            else:
                print("Error pulling updates:", pull_result.stderr.strip())
        else:
            print("Local branch is up to date.")
    except Exception as e:
        print("An error occurred:", str(e))

# Run the function
check_and_update_remote()