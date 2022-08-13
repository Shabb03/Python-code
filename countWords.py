#!/usr/bin/env python3

import sys
from string import punctuation

def count_words(text):
    dic = {}
    for line in text:
        linesplit = line.lower().split()
        for word in linesplit:
            word = word.strip(punctuation)
            if not word:
                continue
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    return dic

try:
    with open(sys.argv[1], 'r') as text_file:
        dic = count_words(text_file)
        for key, value in sorted(dic.items()):
            print(f'{key}: {value}')
except:
    print("No text file provided")
