#!/usr/bin/python
import socket
import argparse
import random
import re
import Queue

par = argparse.ArgumentParser(description='Python Network Scanner',epilog=
        'Remember to ONLY scan targets you have explicit authorization to do so!')
par.add_argument('-p',help='ports to scan, comma seperated',required=False)
par.add_argument('-v',help='verbose output',action='store_true',required=False)
par.add_argument('IP',help='IP of target, supports CIDR notation')

# specify the default ports to scan (min-max)
min_port = 1
max_port = 1024
# set socket timeout
s_timeout = 1

def ip2bin(ip):
    """Convert an IP address from its dotted-decimal format to
        to its 32 binary digit representation"""
    b = ""
    inOcts = ip.split(".")
    outOcts = 4
    for q in inOcts:
        if q != "":
            b += dec2bin(int(q),8)
            outOcts -= 1
    while outOcts > 0:
        b += "00000000"
        outOcts -= 1
    return b

def dec2bin(n,d=None):
    """Convert a decimal number to binary representation
        if d is specified, left-pad the binary number with 0s to that length"""
    s = ""
    while n>0:
        if n&1:
            s = "1"+s
        else:
            s = "0"+s
        n >>= 1
    if d is not None:
        while len(s)<d:
            s = "0"+s
    if s == "": s = "0"
    return s

def bin2ip(b):
    """Convert binary string to ip"""
    ip = ""
    for i in range(0,len(b),8):
        ip += str(int(b[i:i+8],2))+"."
    return ip[:-1]

def calcCIDR(c, tgt_hosts):
    """Store the list of IP addresses based on the CIDR notation specified"""
    parts = c.split("/")
    baseIP = ip2bin(parts[0])
    subnet = int(parts[1])
    # for /32 simply assign the single IP
    if subnet == 32:
        tgt_hosts.append(bin2ip(baseIP))
    # for any other size subnet, create a list of IP addresses by concatenating
    # the prefix with each of the suffixes in the subnet
    else:
        ipPrefix = baseIP[:-(32-subnet)]
        for i in range(2**(32-subnet)):
            tgt_hosts.append(bin2ip(ipPrefix+dec2bin(i, (32-subnet))))

def validateCIDRBlock(cidr_ip):
    """Input validation for the IP/CIDR specified"""
    # appropriate format for CIDR block ($prefix/$subnet)
    c_ip_form = re.compile("^([0-9]{1,3}\.){0,3}[0-9]{1,3}(/[0-9]{1,2}){1}$")
    if not c_ip_form.match(cidr_ip):
        print "Error: Invalid CIDR notation"
        return False
    # extract prefix and subnet size
    ip, subnet = cidr_ip.split("/")
    # each octet must be a value from 1-255
    octets = ip.split(".")
    for p in octets:
        if (int(p) < 0) or (int(p) > 255):
            print "Error: "+str(p)+" is an invalid octet."
            return False
    # subnet is an appropriate value (1-32)
    if (int(subnet) < 1) or (int(subnet) > 32):
        print "Error: "+str(subnet)+" is an invalid subnet size."
        return False
    # passed all checks -> return True
    return True

def printUsage():
    print "Usage: ./portscan.py <IP>/<CIDR>\n\t e.g. ./portscan.py 192.168.1.5/24"

def cidr_calc_main(tgt_input, tgt_hosts):
    # input validation
    if not validateCIDRBlock(tgt_input):
        printUsage()
    # print the user-specified CIDR block
    else:
        tgt_hosts = calcCIDR(tgt_input, tgt_hosts)
        return tgt_hosts
    
def scan(ip, port):
    """Attempt a connection to the target host on specified port"""
    if args.v:
        print 'Scanning '+ip+', port '+str(port)
    s = socket.socket()
    s.settimeout(s_timeout)
    result = s.connect_ex((ip,port))      
    if result == 0:
        print ip+': Port '+str(port)+' open'
        s.close()
    else:
        s.close()

def main():
    tgt_hosts = []
    
    # determine IP range to scan
    tgt_input = args.IP
    if '/' in tgt_input:
        cidr_calc_main(tgt_input, tgt_hosts)
    else:
        tgt_hosts = [tgt_input]

    if args.v:
        print 'Target Hosts: '+str(tgt_hosts)
    
    # determine ports to scan
    if args.p:
        tgt_ports = (args.p).split(',')
    else:
        tgt_ports = range(min_port,max_port)
        
    # randomize ip and port lists
    random.shuffle(tgt_hosts)
    random.shuffle(tgt_ports)
  
    if args.v:
        print 'Target Ports:'+str(tgt_ports)
  

    q = Queue.Queue()
    
    print 'Scanning...\n'
    
    # execute each ip:port scan in a queue
    # using the queue method prevents a file handle overflow
    # when scanning a large number or ports and/or hosts
    for ip in tgt_hosts:
        for port in tgt_ports:
            q.put(scan(ip,int(port)))
        
    print '\nScan complete.'
    
if __name__ == "__main__":
    args = par.parse_args()
    main()