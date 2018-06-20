#!/usr/bin/env python3
import sys
file = sys.argv[1]
input = open(file).read()
chars = input.split()
output = "".join(chr(int(i)) for i in chars)
print(output)
