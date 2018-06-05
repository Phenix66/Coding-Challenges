#!/usr/bin/python
import random, argparse, socket, netaddr, thread

par=argparse.ArgumentParser(description='Simple Python Network Scanner')
par.add_argument('-p',help='specify ports to scan, comma seperated',required=False)
par.add_argument('-Pn',help='Don\'t ping',action='store_true',required=False)
par.add_argument('IP',help='IP of target')
args=par.parse_args()

#def scan(i,p):
    

#Create the IP scan list
net=netaddr.IPNetwork(args.IP)
iplist=list(net)
random.shuffle(iplist)

#Determine ports to scan
if args.p:
    tgtports=(args.p).split(',')
else:
    tgtports=range(1,1024)
    
#Start the scan for each target
print tgtports, iplist
for i in iplist:
    for p in tgtports:
        #print 'Creating thread '+str(i)+':'+str(p)
        s=socket.socket()
        print 'Socket created'
        try:
            print 'Try statement'
            s.connect((str(i),p))
            print 'Connected to '+str(i)+':'+str(p)
            s.close()
        except:
            print 'uh-oh'
