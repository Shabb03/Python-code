#!/usr/bin/env python3

def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

inputList = input("Enter a list of numbers: ")
inputList = inputList.split()
list = [int(x) for x in inputList]
print(sum(list))