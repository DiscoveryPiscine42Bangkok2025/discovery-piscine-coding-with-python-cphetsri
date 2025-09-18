#!/usr/bin/env python3

def main():

    print("Enter a number")
    numeric = int(input())
    i = 0

    while i <= 9:
        print(i, "x", numeric, "=", i*numeric)
        i += 1

main()

