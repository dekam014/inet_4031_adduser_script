#!/usr/bin/python3

# INET4031
# Maati
# 04-15-2026
# 04-15-2026

# os is used to run system-level commands from Python
# re is used for pattern matching (like checking for symbols in text)
# sys allows access to standard input (stdin) so the script can read input lines

import os
import re
import sys


def main():
    for line in sys.stdin:

        # This checks if the line begins with "#"
        # Lines starting with "#" are treated as comments and skipped
        match = re.match("^#",line)

        # This splits each line using ":" to separate the fields (username, password, etc.)
        fields = line.strip().split(':')

        # This condition checks if the line is a comment OR if it doesn't have exactly 5 fields
        # If either is true, the script skips that line
        # This prevents errors from bad or incomplete input lines
        if match or len(fields) != 5:
            continue

        # These lines assign values from the input to variables (username, password, and user info)
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This splits the groups by commas in case the user belongs to multiple groups
        groups = fields[4].split(',')

        # This prints a message showing which user is being created
        print("==> Creating account for %s..." % (username))

        # This builds the Linux command to create a new user with no password initially
        # The gecos field adds user details like name
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # These lines were originally used for a dry run to test output without making changes
        print(cmd)
        os.system(cmd)

        # This prints a message that the password is being set
        print("==> Setting the password for %s..." % (username))

        # This creates a command that sends the password twice (for confirmation)
        # Then pipes it into the passwd command to set the password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        # This runs the password command
        print(cmd)
        os.system(cmd)

        for group in groups:
            # This checks if the group is not "-"
            # "-" means do not add the user to any groups
            # If it is a real group, the user is added to it
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
