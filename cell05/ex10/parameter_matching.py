#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) == 1:
        print("none")

    else:
        parm = sys.argv[1]
        word = input("What was the parameter? ")

        if  word == parm:
            print("Good job!")
        else:
            print("Nope, sorry...")

main()