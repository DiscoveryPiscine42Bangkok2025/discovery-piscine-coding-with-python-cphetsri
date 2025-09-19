#!/usr/bin/env python3

def main():
    orgarr = [2, 8, 9, 48, 8, 22, -12, 2]

    for i in range(len(orgarr)):
        orgarr[i]

    newarr = [x + 2 for x in orgarr]
    print(f"Original array: {orgarr}")
    print(f"New array: {newarr}")
    
main()