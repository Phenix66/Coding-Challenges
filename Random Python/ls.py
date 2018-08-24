#!/usr/bin/python
import os
import sys
import pwd
import grp
import time

try:
    if len(sys.argv[1:]) > 1:
        print("ls only handles one specified directory at a time!")
        print("%s <directory>" % (sys.argv[0]))
        sys.exit(1)
except IndexError:
    pass

# Accept user specified directory, uses current directory otherwise
if len(sys.argv) > 1:
    inputDir = sys.argv[1]
else:
    inputDir = "."

# Get directory listing and sort alphabetically 
files = os.listdir(inputDir)
files_sorted = sorted(files, key=str.lower)

permissionDict ={'0':('---'), '1':('--x'), '2':('-w-'), '3':('-wx'), \
    '4':('r--'), '5':('r-x'), '6':('rw-'), '7':('rwx')}

def perms_calc(file, stat):
    octal = oct(stat.st_mode)[-4:]
    if os.path.isdir(file):
        perms = "d"
    elif os.path.isfile(file):
        perms = "-"
    for n in octal[1:]:
        perms = perms + permissionDict[n]
    specialbit = int(octal[0])
    if specialbit != 0:
        if specialbit >= 4:
            if perms[3] == "x":
                perms = perms[:3] + "s" + perms[4:]
            elif perms[3] == "-":
                perms = perms[:3] + "S" + perms[4:]
        if specialbit == 2 or octal[0] == 6:
            if perms[6] == "x":
                perms = perms[:6] + "s" + perms[7:]
            elif perms[6] == "-":
                perms = perms[:6] + "S" + perms[7:]
        if specialbit == 1:
            perms = perms[:9] + "t"
    return perms

# Define colors by name for easy reference
LTBLUE = '\033[96m'
LTGREEN = '\033[92m'
WHITE = '\033[97m'

def colorize(modestr, color = WHITE):
    if modestr[0] == "d":
        # Is a directory
        color = LTBLUE
    elif modestr.find("x") > -1:
        # Is a file
        color = LTGREEN
    return color

for file in files_sorted:
    # Absolute path
    fullname = "%s/%s" % (inputDir, file)
    # Gets file info
    stat = os.stat(fullname)
    perms = perms_calc(fullname, stat)
    color = colorize(perms)
    nlink = stat.st_nlink
    uid = stat.st_uid
    gid = stat.st_gid
    user = (pwd.getpwuid(uid))[0]
    group = (grp.getgrgid(gid))[0]
    size = stat.st_size
    lastmodified = time.localtime(os.path.getmtime(fullname))
    mod_time = time.strftime("%b %d %H:%M", lastmodified)
    print("%s %3s %6s %6s %8s %s %s %s \033[0m" % (perms, nlink, user, group, size, mod_time, color, file))
