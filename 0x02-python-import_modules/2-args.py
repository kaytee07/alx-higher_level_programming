#!/usr/bin/python3
from sys import argv
arglen = len(argv)
if arglen == 1:
    print("{} arguments.".format(arglen - 1))
else:
    print("{} arguments:".format(arglen - 1))
    for i in range(arglen-1):
        print("{}: {}".format(i+1, argv[i+1]))
