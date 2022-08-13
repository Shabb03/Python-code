#!/usr/bin/env python3

def reverseList(list, newList=None):
    if newList is None:
        newList = []
    if list == []:
        return newList
    newList.append(list.pop())
    return reverseList(list, newList)

inputList = input("Enter a list of numbers: ")
inputList = inputList.split()
list = [int(x) if x.isdigit() else x for x in inputList]
print(reverseList(list))