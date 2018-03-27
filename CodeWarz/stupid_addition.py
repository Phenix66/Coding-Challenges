#!/usr/bin/env python3.6
import sys
from decimal import *
file = sys.argv[1]
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f]
for x in lstInput:
    if " " in x:
        a,b = x.split(" ")
        try:
            a = Decimal(a)
            b = Decimal(b)
            result = a + b
            print(result)
        except:
            continue