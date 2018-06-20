#!/usr/bin/env python3.6
import sys
from decimal import *
file =  sys.argv[1]
lstInput = []
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f]
for c in lstInput:
    a,b = c.split(" ") #Separate each pair
    a = Decimal(a)
    b = Decimal(b)
    result = a + b
    print(result)
