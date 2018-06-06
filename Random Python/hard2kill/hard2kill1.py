#!/usr/bin/python

import os
import sys
import time
import shutil
import tempfile

tempname = tempfile.mktemp(prefix="tmpdfh")
shutil.copy(sys.argv[0], tempname)
os.system("touch ALIVE1.txt")
time.sleep(1)
os.system("%s &" % (tempname))

time.sleep(1)
os.remove(tempname)
