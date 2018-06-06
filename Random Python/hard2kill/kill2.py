#!/usr/bin/python
import os
import sys
import string

tgt = "adj"
f = os.popen("ps aux")
lines = f.readlines()
while True:
    os.system("rm -rf /tmp/a*")
    for line in lines:
        tokens = line.split()
        pidstr = tokens[1]
        cmd = tokens[-1]
        if tgt == cmd[-9:-12]:
            pid = string.atoi(pidstr)
            os.system("rm -rf %s" % (cmd[-12:]))
            os.kill(pid, 9)
