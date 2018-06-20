#!/usr/bin/env python3
import sys

file = sys.argv[1]
lines = []
with open(file, "r") as f:
    lines = f.readlines()
    
for line in lines:
    nums = line.split()
    sum = 0
    for n in nums:
        sum = sum + int(n, 2)
    print(sum)
