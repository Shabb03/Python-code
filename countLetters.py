#!/usr/bin/env python3

def countLetters(s):
    if s == "":
        return 0
    return 1 + countLetters(s[:-1])

string = input("Enter a word: ")
print(countLetters(string))