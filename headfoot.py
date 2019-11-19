#!/usr/bin/env python3

# Import regex
import re

# Source and Target List
source = 'index.html'
targets = ['info.html','volunteers.html','press.html','schedule.html']

# Go through targets and replace
for target in targets:
    s = open(source,'r') # Open source file
    html = s.read() # Read file
    s.close() # Close File
    header = html.split('<!-- Main -->')[0] # Find Header
    footer = html.split('<!-- Footer -->')[-1] # Find Footer

    t = open(target,'r+') # Open target file
    body = t.read().split('<!-- Main -->')[1].split('<!-- Footer -->')[0] # Identify body of file
    t.seek(0) # Go to start of file
    t.write(header+'<!-- Main -->'+body+'<!-- Footer -->'+footer) # Write body w/ source header and footer
    t.truncate() # Get rid of the rest
    t.close() # Close file