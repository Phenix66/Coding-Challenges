#!/usr/bin/python

# Takes at least 2 arguments and multiplies them

import sys
import string

lstValues = []
result = 0

for x in sys.argv[1:]:
    try:
        lstValues.append(string.atoi(x))
    except ValueError:
        try:
            lstValues.append(string.atof(x))
        except ValueError:
            print "This program accepts integers or floats only!"
            sys.exit(1)

try:
    result = lstValues[0] * lstValues[1]
except IndexError:
    print "You must enter at least two numbers!"
    sys.exit(1)

try:
    for x in lstValues[2:]:
        result = result * x
except:
    pass

print "The result is %s" % (result)
