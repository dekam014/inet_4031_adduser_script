# INET4031 Add Users Script and User List

## Program Description
This program helps create multiple Linux users at once using a file instead of doing everything manually. Instead of typing commands for each user, the script reads a list and creates the users and their groups automatically. This saves time and helps avoid mistakes.

Normally, you would have to use commands like useradd, adduser, groupadd, and usermod for every single user. You would also need to set passwords and assign groups one by one. This script does all of that for you by using the information from an input file and running those same commands automatically.


## Program User Operation
This program works by reading user information from the create-users.input file. The script goes through the file one line at a time, splits up the information, and then runs the commands needed to create each user and assign groups.

To use the program, make sure both create-users.py and create-users.input are in the same folder. You may need to make the script executable before running it. It’s a good idea to do a dry run first to make sure everything looks correct before actually creating users.

### Input File Format
The create-users.input file has one user per line. Each line uses colons to separate the fields in this order:
