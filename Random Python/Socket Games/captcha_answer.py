#!/usr/bin/python
import socket
import os
import sys
sys.path.append('../')
from modules import word2number as w2n
from modules import num2words as n2w

IP = "127.0.0.1"
PORT = 12345

s = socket.socket()
s.connect((IP, PORT))

def recv_all():
    received_data = s.recv(1024)
    data = (received_data.split())[-6:]
    for x in data:
        print x,
    print " "
    return data

def send_all(data):
    s.sendall(data)
    print data + "\n"
    return

while True:
    data = recv_all()
    try:
        numword1 = data[3]
        numword2 = data[5].strip("?")
        num1 = w2n.word_to_num(numword1)
        num2 = w2n.word_to_num(numword2)
        sum = num1 + num2
        sumword = n2w.int2word(sum)
        send_all(sumword)
    except ValueError:
        break
    except IndexError:
        if data == []:
            break
