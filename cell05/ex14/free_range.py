#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) == 1:
        print("none")

    else:
        parmst = int(sys.argv[1])
        parmlst = int(sys.argv[2])
        n = list(range(parmst, parmlst + 1))
        print(n)

main()