#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            toScreen = chr(int(ord(i)) - 32)
        else:
            toScreen = i
        print(f"{toScreen}", end="")
    print()
