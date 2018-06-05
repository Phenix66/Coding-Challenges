#!/usr/bin/python
import sys

logfile = "./logfile.txt"

try:
    with open(logfile, "a+") as f:
        while True:
            data = raw_input("Enter data to be logged: ")
            if not len(data) == 0:
                f.write(data + "\n")
            else:
                print "Nothing logged"
except IOError, err:
    print err
