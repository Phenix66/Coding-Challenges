#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',80))

while True:
    msg,addr = s.recvfrom(4096)
    # Remember to decode in reverse order of encoding!
    data = msg.decode("base64").decode("bz2")
    print data
