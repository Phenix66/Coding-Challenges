#!/usr/bin/python
import sys
from decimal import Decimal

file = sys.argv[1]
csv = []
with open(file, "r") as f:
    csv = f.readlines()

for line in csv:
    values = line.split(",")
    result = sum(Decimal(v) for v in values)
    print(result)
