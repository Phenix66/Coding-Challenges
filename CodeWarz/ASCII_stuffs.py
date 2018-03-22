#!/usr/bin/env python3.6
import sys, binascii
file = sys.argv[1]
input = open(file).read()
a = input.replace(' ','')
decoded = binascii.unhexlify(a)
b = decoded.decode(encoding="utf-8")
print(b)