#!/usr/bin/env python3

space = " "
a = "*"
n = int(input("Enter width of Diamond:  "))
i = 1

while i <= n:
    print(((space * (n - i)) + ((a + space) * i)).rstrip())
    i += 1
while i < (n * 2):
    print(((space * (i - n)) + ((a + space) * ((n * 2) - i))).rstrip())
    i += 1