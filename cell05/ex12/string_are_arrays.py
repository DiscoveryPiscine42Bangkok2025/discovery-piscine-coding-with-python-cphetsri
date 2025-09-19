#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) != 2:
        print("none")
    else:
        word = sys.argv[1]
        result = "".join([ch for ch in word if ch == "z"])
        if result:
            print(result)
        else:
            print("none")

main()