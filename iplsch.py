# Import regular expressions.
import re

# Create an empty array object (LIST).
ipList = []

# File to use as baseline. e.g. List from Marius.
with open('base.txt', "r") as file1:
    # Simple for each line in file
    for line in file1:
        # Sanitise line/string and push it to array.
        ipList.append(line.strip())

# File to use query against baseline. e.g. List from UFW.
# https://github.com/poddmo/ufw-blocklist
with open('test.txt', "r") as file2:
    # Simple for each line in file
    for line in file2:
        # Assign variable to regex filter of line/string (IP).
        ipAddr = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )[0]
        # Evaluate if the string (IP) exists within the array (LIST).
        if ipAddr not in ipList:
            # If the above condition is true,
            # split the string (IP) off to a variable.
            d = line.split()
            # Finally, print out the result on the screen.
            print('Missing:', d[0])
