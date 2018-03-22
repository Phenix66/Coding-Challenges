#!/usr/bin/env python3.6
import sys
x=0
for i in sys.argv:
    if x == 0:
        x += 1
    else:
        print(i, end=" ")
        x += 1