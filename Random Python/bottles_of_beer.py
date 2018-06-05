#!/usr/bin/python
from time import sleep
for x in range(99,0,-1):
    print(str(x) + " bottles of beer on the wall")
    print(str(x) + " bottles of beer")
    print("Take one down, pass it around")
    if x == 1:
        print("Bar's close y'all, no more beer!")
    else:
        print(str(x-1) + " bottles of beer on the wall")
    print " "
    sleep(2)
