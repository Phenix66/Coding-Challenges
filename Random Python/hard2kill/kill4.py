#!/usr/bin/python
import os
import sys
import string

tgt = "11940"
while True:
    f = os.popen("ps aux")
    lines = f.readlines()
    for line in lines:
        tokens = line.split()
        pidstr = tokens[1]
        cmd = tokens[-1]
        vsz = tokens[4]
        if tgt == vsz:
            file = cmd[17:]
            os.system("sudo rm -rf %s" % (file))
            pid = string.atoi(pidstr)
            os.system("sudo kill -9 %s" % (pidstr))
