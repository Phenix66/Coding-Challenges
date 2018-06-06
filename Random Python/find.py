#!/usr/bin/python
import os
import sys
import fnmatch

def recursive_search(inputDir, fileName):
    results = []
    match = "*" + fileName + "*"
    currentDir = os.path.abspath(inputDir)
    files = os.listdir(inputDir)
    for file in files:
        # By default it attempts relative path, we must force absolute path names
        fullname = ("%s/%s") % (inputDir, file)
        if os.path.isdir(fullname):
            nextDir = "%s/%s" % (currentDir, file)
            try:
                results += recursive_search(nextDir, fileName)
            except:
                # Usually permission denied, so we just move on
                pass
        elif fnmatch.fnmatch(file, match):
            fullpath = os.path.abspath("%s/%s" % (inputDir, file))
            results.append(fullpath)
    return results

def usage():
    print "%s <filename> [<directory>]" % (sys.argv[0])
    sys.exit(1)

if __name__ == "__main__":
    if not len(sys.argv[1:]) >= 1:
        if len(sys.arv[1:]) > 2:
            print "Too many arguments!"
            usage()
        else:
            print "Please provide at least a filename to search for!"
            usage()

    fileName = sys.argv[1]
    try:
        inputDir = sys.argv[2]
    except IndexError:
        inputDir = "./"

    try:
        results = recursive_search(inputDir, fileName)
    except OSError, err:
        print err

    if len(results) == 0:
        print "No results found"
    else:
        for x in results:
            print x
