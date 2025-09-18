#!/usr/bin/env python3

def main():
    
    print("Enter the first number:")
    firstnum = int(input())
    
    print("Enter the second number:")
    secondnum = int(input())

    result = firstnum * secondnum
    print(firstnum, "x", secondnum, "=", result)

    if result > 0:
        print("The result is positive.")

    elif result == 0:
        print("The reult is positive and negative.")

    elif result < 0:
        print("The result is negative.")

main()