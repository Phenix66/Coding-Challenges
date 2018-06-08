#!/usr/bin/python
import os
import sys
from subprocess import Popen, PIPE, STDOUT

def hash(fullpath):
    cmd = "md5sum %s" % (fullpath)
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    if "No such file or directory" in output:
        # md5sum returning this error indicates a file was deleted
        return "null"
    else:
        (md5, fullname) = output.split()
        return md5

def load_hashes(mydir, dictHashes):
    # Loads hashes if they exist
    try:
        with open("./hashes.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                (val, key) = line.strip().split()
                dictHashes[key] = val
    except IOError:
        dictHashes = gen_hashes(mydir)
    return dictHashes

def write_hashes(dictHashes):
    # Updates (or creates) hash file in current directory
    with open("./hashes.txt", "w") as f:
        for key, val in dictHashes.iteritems():
            line = "%s %s\n" % (val, key)
            f.write(line)

def gen_hashes(mydir):
    # Creates starting values if hash file did not exist
    dictHashes = {}
    files = []
    filenames = os.listdir(mydir)

    for file in filenames:
        fullpath = "%s/%s" % (mydir, file)
        if os.path.isfile(fullpath):
            files.append(fullpath)

    for filename in files:
        dictHashes[filename] = hash(filename)
    return dictHashes

def monitor(dictHashes):
    # Continually check for changes
    while True:
        files = []
        filenames = os.listdir(mydir)

        for file in filenames:
            fullpath = "%s/%s" % (mydir, file)
            if os.path.isfile(fullpath):
                files.append(fullpath)

        for filename in files:
            try:
                currentHash = hash(filename)
                if filename in dictHashes:
                    if currentHash == "null":
                        print "%s has been deleted!" % (filename)
                        del dictHashes[filename]
                    else:
                        if currentHash != dictHashes[filename]:
                            print "%s has changed!!" % (filename)
                            dictHashes[filename] = currentHash
                else:
                    print "New file created!! %s" % (filename)
                    dictHashes[filename] = currentHash
            except ValueError:
                pass

if __name__ == "__main__":
    # Allows user to specify directory to monitor. Defaults to current directory.
    if len(sys.argv) == 1:
        mydir = os.path.abspath(".")
    elif len(sys.argv) == 2:
        mydir = os.path.abspath(sys.argv[1])
    else:
        print "Too many arguments provided.\n%s [<directory>]" % (sys.argv[0])
        sys.exit(1)

    dictHashes = {}

    try:
        dictHashes = load_hashes(mydir, dictHashes)
        monitor(dictHashes)
    except KeyboardInterrupt:
        confirm = raw_input("\nWrite changed hashes to disk? (Y/n) ")
        if confirm.lower == "n" or confirm.lower == "no":
            sys.exit(0)
        else:
            write_hashes(dictHashes)
            sys.exit(0)
