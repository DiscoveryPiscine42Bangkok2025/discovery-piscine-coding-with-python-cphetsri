#!/usr/bin/env python3

def main():
    orgarr = [2, 8, 9, 48, 8, 22, -12, 2]
    newarr = set()

    for i in orgarr:
        if i > 5:
            newarr.add(i + 2)

    print(orgarr)
    print(newarr)
    
main()