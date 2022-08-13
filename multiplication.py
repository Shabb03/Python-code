#!/usr/bin/env python3

n = int(input("Enter a number between 0-99:  "))

if n < 100 and n > -1:
    for i in range(1, 13):
        print(f'{n:2d} * {i:2d} = {n*i:4d}')
else:
    print("Invalid Number!")