#!/usr/bin/env python3

import sys

with open("words.txt") as f, open("words2.txt", "w") as output:
    for line in f.readlines():
        line = line.strip()
        print(line)
        if len(line) > 5:
            #print(line)
            output.write(line)
            output.write("\n")