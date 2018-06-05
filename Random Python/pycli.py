#!/usr/bin/python
import socket
import struct
import os
import argparse

par = argparse.ArgumentParser(description='Simple Socket Commands')
par.add_argument('IP')
par.add_argument('PORT')
args = par.parse_args()

#Sets buffer size
buff=1024

def recv_all(sock,n):
    data = ''
    while len(data) < n:
        p = sock.recv(n-len(data))
        if not p:
            return None
        data += p
    return data

def recv_data(sock):
    msglen = recv_all(sock,4)
    if not msglen:
        return None
    mlen = struct.unpack('>I',msglen)[0]
    return recv_all(sock,mlen)

def send_data(sock,data):
    msg = struct.pack('>I',len(data))+data
    sock.sendall(msg)

s = socket.socket()
s.connect((args.IP,int(args.PORT)))
msg = recv_data(s)
print msg

while True:
    data = raw_input('Type a command: ')
    send_data(s,data)
    if not data:
        break
    inc = recv_data(s)
    if not inc:
        break
    print '\n'+inc