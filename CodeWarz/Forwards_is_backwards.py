#!/usr/bin/env python3.6
import sys
file = sys.argv[1]
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f]
for x in lstInput:
    if x == x[::-1]:
        print('True')
    else:
        print('False')