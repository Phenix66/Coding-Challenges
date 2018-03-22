#!/usr/bin/env python3.6
import sys
import math
file = sys.argv[1]
lstInput=[]
with open(file, 'r') as f:
    lstInput = [line.strip() for line in f] #Reads each line and stores in the list, stripping the 'newline' char
lstInput=[int(x) for x in lstInput] #convert strings to integers
lstInput.sort() #not really necessary, oh well
def rounddown(y):
    return int(math.floor(y/10.0))*10 #rounds each integer down to it's base 10 unit
lstInput=[rounddown(y) for y in lstInput] #apply above to entire list
lstTally=[0] * ((max(lstInput)//10)+1)
a=0
for b in lstInput: #For each item, determine which group of tens to tally and add
    a=b//10
    lstTally[a]+=1
d=''
for c in lstTally:
    d=d+str(c)
print(d) #Final out displays a tally of how many instances of each group of 10s (0-9, 10-19,so on) occurred in the input, from left to right.