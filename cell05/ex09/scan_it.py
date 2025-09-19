#!/usr/bin/env python3

import sys
import re

def main():

    if len(sys.argv) <= 2:
        print("none")
    else:
        keyword = sys.argv[1]
        sentence = sys.argv[2]
        countkey = re.findall(keyword, sentence)

        print(len(countkey))

main()