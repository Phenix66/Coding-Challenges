#!/usr/bin/env python3.6
import sys
import math
file = sys.argv[1]
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f]
for c in lstInput:
    a,b = c.split(" ") # Separate each pair
    a = float(a)
    b = float(b)
    count = a
    lstResults = []
    while count <= b:
        if math.fmod( count, 7 ) == 0: # Determine if the current test value (counter) is divisible by 7
            if math.fmod( count, 5 ) != 0: # Make sure current test value is not divisible by 5
                lstResults.append(int(count))
            count+=1
        else:
            count+=1
    print(','.join(str(x) for x in lstResults))