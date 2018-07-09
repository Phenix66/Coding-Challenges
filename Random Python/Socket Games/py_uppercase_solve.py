#!/usr/bin/python
import sys
import socket

IP = sys.argv[1]
PORT = int(sys.argv[2])

s = socket.socket()
s.connect((IP, PORT))

challenge = (s.recv(4096).split("\n"))[1]
response = challenge.upper()

s.send(response)

answer = s.recv(4096)
print answer
