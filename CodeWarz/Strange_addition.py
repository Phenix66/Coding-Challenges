#!/usr/bin/env python3
import sys
file = sys.argv[1]
with open(file, "r") as f:
    lstLines = f.readlines()
        
for line in lstLines:
    nums = line.split()
    sum = 0
    for n in nums:
        sum = sum + int(n)
    sum = sum + len(nums)
    print(sum)
