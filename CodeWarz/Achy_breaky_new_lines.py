#!/usr/bin/env python3
import sys

file = sys.argv[1]
lstLines = []
with open(file, "r") as f:
    lines = f.readlines()
    for line in lines:
        lstLines.append(line.strip())
        
for x in lstLines:
    if len(x) > 1:
        print(x)
