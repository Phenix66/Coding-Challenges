#!/usr/bin/env python3.6
import sys
file = sys.argv[1]
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f]
lstValues = [words for segments in lstInput for words in segments.split()] # Separates each encoded character individually 
for x in lstValues:
    if "0x" in x:
        x = x.replace("0x", "")
        y = chr(int(x, base=16))
        print(y, end='')
    elif "0b" in x:
        x = x.replace("0b", "")
        y = chr(int(x, base=2))
        print(y, end='')
    elif x.startswith('0'):
        y = chr(int(x, base=8))
        print(y, end='')
    else:
        y = chr(int(x))
        print(y, end='')