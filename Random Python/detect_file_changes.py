#!/usr/bin/python
import os
import sys

dictHashes = {}

def hash(fullpath):
    cmd = "md5sum %s" % (fullpath)
    f = os.popen(cmd)
    line = f.read().strip()
    (md5, fullname) = line.split()
    return md5

def load_hashes(files):
    # Loads hashes if they exist
    try:
        with open("./hashes.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                (val, key) = line.strip().split()
                dictHashes[key] = val
    except:
        gen_hashes(files)

def write_hashes():
    # Updates (or creates) hash file in current directory
    with open("./hashes.txt", "w") as f:
        for key, val in dictHashes.iteritems():
            line = "%s %s\n" % (val, key)
            f.write(line)

def gen_hashes(files):
    # Creates starting values
    for filename in files:
        dictHashes[filename] = hash(filename)

def monitor(files):
    # Continually check for changes
    while True:
        for filename in files:
            try:
                currentHash = hash(filename)
                if filename in dictHashes:
                    if currentHash != dictHashes[filename]:
                        print "%s has changed!!" % (filename)
                        dictHashes[filename] = currentHash
                else:
                    print "New file created!! %s" % (filename)
                    dictHashes[filename] = currentHash
            except ValueError:
                pass

if __name__ == "__main__":
    if len(sys.argv) == 1:
        mydir = os.path.abspath(".")
    elif len(sys.argv) == 2:
        mydir = os.path.abspath(sys.argv[1])
    else:
        print "Too many arguments provided.\n%s [<directory>]" % (sys.argv[0])
        sys.exit(1)

    files = []
    filenames = os.listdir(mydir)

    for file in filenames:
        fullpath = "%s/%s" % (mydir, file)
        if os.path.isfile(fullpath):
            files.append(fullpath)

    try:
        load_hashes(files)
        monitor(files)
    except KeyboardInterrupt:
        confirm = raw_input("\nWrite changed hashes to disk? (Y/n) ")
        if confirm.lower == "n" or confirm.lower == "no":
            sys.exit(0)
        else:
            write_hashes()
            sys.exit(0)
