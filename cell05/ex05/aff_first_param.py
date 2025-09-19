#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) == 1:
        print("none")
    else:
        parm = sys.argv[1]
        print(parm)

main()