#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) <= 2:
        print("none")
    else:
        for x in reversed(sys.argv[1:]):
            print(x)

main()