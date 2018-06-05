#!/usr/bin/python
import sys
import os.path

if not len(sys.argv[0:]) == 3:
    print "Please provide exactly 2 filenames, source and destination"
    print "%s <source> <destination>" % (sys.argv[0])
    sys.exit(1)

src = sys.argv[1]
dst = sys.argv[2]

def mycopy():
    with open(src, "r") as s:
        with open(dst, "w+") as d:
            size = 100
            while size == 100:
                data = s.read(100)
                size = len(data)
                d.write(data)

try:
    confirm = "n"
    if os.path.exists(dst):
        if os.path.isfile(dst):
            confirm = raw_input("Destination file exists, do you want to overwrite? (y/N) ")
            if confirm.lower() == "y" or confirm.lower() == "yes":
                mycopy()
            elif confirm.lower() == "n" or confirm.lower() == "no":
                print "Skipping copy"
            else:
                print "Invalid overwrite option specified, skipping copy"
        else:
            mycopy()
        if os.path.isdir(dst):
            print "Cannot overwrite directory"
            sys.exit(1)
    else:
        print "Desination path does not exist"
except IOError, err:
    print err
    sys.exit(1)
