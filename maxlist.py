#!/usr/bin/env python3

def maxlist(list):
    if len(list) == 1:
        return list[0]
    head = list[0]
    tail = maxlist(list[1:])
    return head if head > tail else tail

inputList = input("Enter a list of numbers: ")
inputList = inputList.split()
list = [int(x) for x in inputList]
print(maxlist(list))