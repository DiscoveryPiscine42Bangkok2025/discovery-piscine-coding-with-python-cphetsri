#!/usr/bin/env python3

def main():
    curage = int(input("Please tell me your age: "))
    print(f"You are currently {curage} years old.")

    i = 1
    while i <= 3:
        print(f"In {i*10} years, you'll be {curage + (i * 10)} years old.")
        i += 1
main()