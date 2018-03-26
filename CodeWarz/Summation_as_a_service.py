#!/usr/bin/env python3.6
import sys
file =  sys.argv[1]
lstInput = []
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f]
lstPairs = []
for c in lstInput:
    a,b = c.split(" ") #Separate each pair
    a = int(a)
    b = int(b)
    lstPairs.append([a,b])
def summation( a, b ):
    count = a
    runningTotal = 0
    while count <= b:
        runningTotal = runningTotal + count
        count += 1
    return runningTotal
results = []
for x in lstPairs:
    if x[0] < x[1]:
        results.append(summation(x[0],x[1]))
    else:
        results.append(summation(x[1],x[0]))
for x in results:
    print(x)