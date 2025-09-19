#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) == 1:
        print("none")
    
    else:
        parm = sys.argv[1:]
        print(f"parameters: {len(parm)}")
        for x in parm:
            print(f"{x}: {len(x)}")

main()