#!/usr/bin/env python3

from random import sample

max = input("Enter the maximum number: ")
count = input("Enter the size of the list")

rnums = sample(range(max), count)
print(rnums)