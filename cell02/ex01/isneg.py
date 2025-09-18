#!/usr/bin/env python3

def main():
    num = int(input())

    if num == 0:
        print("This number is both positive and negative")
    elif num < 0:
        print("This number is negative")
    elif num > 0:
        print("This number is positive")

main()