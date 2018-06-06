#!/usr/bin/python
import os
import sys
import string

tgt = "/usr/bin/python /tmp/"
f = os.popen("ps aux")
lines = f.readlines()
while True:
    os.system("rm -rf /tmp/*")
    for line in lines:
        tokens = line.split()
        pidstr = tokens[1]
        cmd = tokens[-1]
        if tgt == cmd[:22]:
            pid = string.atoi(pidstr)
            os.kill(pid, 9)
