#!/usr/bin/python
from scapy.all import *
from threading import Thread
import argparse, netaddr

par=argparse.ArgumentParser(description='Scapy Python Network Scanner')
par.add_argument('-p',help='specify ports to scan, comma seperated',required=False)
par.add_argument('IP',help='IP of target')

args=par.parse_args()
threads = []

#Create the IP scan list
net=netaddr.IPNetwork(args.IP)
iplist=list(net)
random.shuffle(iplist)

#Determine ports to scan
if args.p:
    tgtports=(args.p).split(',')
else:
    tgtports=range(1,1024)
    
def p_scan(ip,port):
    try:
        #Attempt a SYN connect with target host on target port
        s=sr1(IP(dst=ip)/TCP(dport=port,flags='S'),timeout=1,verbose=0)
        if s:
            print ip+': Port '+str(port)+' open'
    except:
        pass

print 'Running scan...'        
for i in iplist:
    for p in tgtports:
        t = Thread(target=p_scan, args=(i,int(p),))
        threads.append(t)
        t.start()
	
[x.join() for x in threads]
print 'Scan complete'
