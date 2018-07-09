#!/usr/bin/python
# Outputs the contents of a file, similar to linux "cat" command
import sys

lstFiles = []

if not len(sys.argv[0:]) < 2:
    for x in sys.argv[1:]:
        lstFiles.append(x)

    for n in lstFiles:
        try:
            with open(n, "r") as f:
                size = 100
                while size == 100:
                    data = f.read(100)
                    size = len(data)
                    sys.stdout.write(data)
        except IOError, err:
            print err

    print " "
else:
    print "Please provide at least one file name"
