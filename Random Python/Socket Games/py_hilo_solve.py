#!/usr/bin/python
import sys
import socket

IP = sys.argv[1]
PORT = int(sys.argv[2])
maxnum = 1000
minnum = 1
guess = 500

s = socket.socket()
s.connect((IP, PORT))

counter = 1
s.recv(4096)
s.send(str(guess))
while counter < 10:
    response = s.recv(4096)
    print response
    if "Higher..." in response:
        minnum = guess
        guess = guess + ((maxnum - minnum)/2)
    elif "Lower..." in response:
        maxnum = guess
        guess = guess - ((maxnum - minnum)/2)
    s.send(str(guess))
    counter += 1
