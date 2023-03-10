#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    if (len(argv) == 1):
        print("{}1".format(total))
    else:
        for i in argv[1:]:
            total += int(i)
    print("{}".format(total))
