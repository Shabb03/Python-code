#!/usr/bin/env python3

import pyshorteners as sh

link = input("Enter link: ")
s = sh.Shortener()
print(s.tinyurl.short(link))