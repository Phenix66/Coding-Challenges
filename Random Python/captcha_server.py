#!/usr/bin/python

import os
import md5
import sys
import time
import random
import socket

# Returns True if user answered question correctly
# and within 1 second
def question(conn):
    nums=['zero', 'one', 'two', 'three', 'four', 
          'five', 'six', 'seven', 'eight', 'nine',
          'ten', 'eleven', 'twelve', 'thirteen', 
          'fourteen', 'fifteen', 'sixteen', 'seventeen',
          'eighteen']
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    total = a + b
    conn.send("How much is %s plus %s?\n" % (nums[a], nums[b]))
    begin = time.time()
    answer = conn.recv(100)
    seconds = time.time() - begin
    if(answer.strip()!=nums[total]):
        conn.send("Wrong answer.\n")
        return False
    if(seconds > 1.0):
        conn.send("Right answer, but too slow.\n")
        return False
    return True
        
HOST = ''
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while(True):
    print "\nListening for new connection..."
    # The accept() line blocks until a call is received
    conn, addr = s.accept()
    print "Connection received: ", addr[1]

    conn.send("This captcha system is designed to thwart computers\n")
    conn.send("Prove you are a human by answering three questions:\n")

    count = 3
    val = True
    while(count>0 and val==True):
        val = question(conn)
        count = count - 1
    if(val):
        conn.send("Congratulations! You have proved you are a human!\n\n")
        conn.send("Flag: %s\n" % md5.new("ASD").hexdigest())
    conn.close()





