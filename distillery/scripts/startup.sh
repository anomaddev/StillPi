#! /bin/sh
export version="0.0.2"

# Start the distillery application
cd StillPi/distillery

# Show the splash screen
python3 -c'import display; display.start_screen(${!version})'