#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arglen = len(argv)
    if arglen == 1:
        print("{} arguments.".format(arglen - 1))
    elif arglen == 2:
        print("{} argument:".format(arglen - 1))
        print("{}: {}".format(arglen-1, argv[arglen-1]))
    else:
        print("{} arguments:".format(arglen - 1))
        for i in range(arglen-1):
            print("{}: {}".format(i+1, argv[i+1]))
