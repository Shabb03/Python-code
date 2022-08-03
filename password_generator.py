#!/usr/bin/env python3

import sys
import random
import string

with open("words2.txt") as f:
    words = f.read().split()

digits = list(string.digits)
special_characters = list("!@#$%^&*()")

def main():
	password = []
	
	i = random.randint(0, len(words))
	j = random.randint(100, 1000)
	password.append(words[i].capitalize())
	password.append(str(j))
	password.append(random.choice(special_characters))

	print("".join(password))

if __name__=="__main__":
	main()