#!/usr/bin/env python3.6
import sys
file = sys.argv[1]
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f]
for x in lstInput:
    lstSentences = x.split(". ")
lstCode = []
for x in lstSentences:
    y = x.partition(" ")[0]
    lstCode.append(y)
print(' '.join(str(x) for x in lstCode))