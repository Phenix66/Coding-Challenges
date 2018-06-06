#!/usr/bin/python
import os
import sys
import string

tgt = "tmpdfh"
f = os.popen("ps aux")
lines = f.readlines()
for line in lines:
    tokens = line.split()
    pidstr = tokens[1]
    cmd = tokens[-1]
    if tgt == cmd[-12:-6]:
        pid = string.atoi(pidstr)
        os.kill(pid, 9)
