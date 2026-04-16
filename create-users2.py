#!/usr/bin/python3

# INET4031
# Kirubail
# 03-26-2026
# 03-02-2026

# os is used to run system commands
# re is used to check patterns in lines
# sys is used to read input from stdin

import os
import re
import sys


def main():

    # Ask user if this is a dry run
    choice = input("Dry run? (Y/N): ").strip().upper()
    dry_run = (choice == "Y")

    for line in open("create-users.input"):

        # Check if line starts with "#" (comment)
        match = re.match("^#",line)

        # Split line into parts using ":"
        fields = line.strip().split(':')

        # Skip bad or commented lines
        if match or len(fields) != 5:
            if dry_run:
                print("Skipping line:", line.strip())
            continue

        # Store user info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Split groups (can be multiple)
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)

                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
