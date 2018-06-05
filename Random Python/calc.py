#!/usr/bin/python
import sys
import string
import getopt

lstInput = []

def add(x):
    sum = x[0]
    for i in x[1:]:
        sum = sum + i
    return sum

def sub(x):
    diff = x[0]
    for i in x[1:]:
        diff = diff - i
    return diff

def multi(x):
    result = x[0]
    for i in x[1:]:
        result = result * i
    return result

def divide(x):
    quotient = x[0]
    try:
        for i in x[1:]:
            quotient = quotient / i
        return quotient
    except ZeroDivisionError:
        print "Stop trying to end the world!\n(Don't divide by zero)"
        sys.exit(1)

def help():
    print "%s -asmd <number1> <number2> ..." % (sys.argv[0])

def app(a):
    try:
        lstInput.append(int(x))
    except:
        try:
            lstInput.append(float(x))
        except:
            print "Invalid values provided."
            help()
            sys.exit(1)

if not len(sys.argv[0:]) > 3:
    print "Not enough values provided"
    help()
    sys.exit(1)

try:
    opts, args = getopt.getopt(sys.argv[1:], 'asmdh')
    for o,a in opts:
        if o == '-a':
            for x in sys.argv[2:]:
                app(x)
            print add(lstInput)
        if o == '-s':
            for x in sys.argv[2:]:
                app(x)
            print sub(lstInput)
        if o == '-m':
            for x in sys.argv[2:]:
                app(x)
            print multi(lstInput)
        if o == '-d':
            for x in sys.argv[2:]:
                app(x)
            print divide(lstInput)
        if o == '-h':
            help()
except getopt.GetoptError:
    print "Invalid option"
    sys.exit(1)
