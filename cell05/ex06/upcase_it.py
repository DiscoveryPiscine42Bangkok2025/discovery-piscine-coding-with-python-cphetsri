#!/usr/bin/env python3

import sys

def main():

    if len(sys.argv) == 1:
        print("none")
    else:
        word = sys.argv[1]
        upword = word.upper()

        print(upword)

main()