#!/usr/bin/python3
for i in range(122, 64, -1):
    char = chr(i)
    if i % 2 == 0:
        print(char.upper(), end='')
    else:
        print(char.lower(), end='')
