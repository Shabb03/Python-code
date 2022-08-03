#!/usr/bin/env python3

import re

def main():
   email = input("Email Address: ").strip()

   m = re.search(r"\d", email)

   index1 = email.index('.')
   index2 = email.index('@')

   username = email[:index2]
   firstname, lastname = username[:index1], username[index1+1:m.start()]
   domain = email[index2+1:]

   #print("Email address: ", email)
   #print("Username: ", username)
   print("Name:", firstname.capitalize(), lastname.capitalize())
   print("Domain name:", domain)

if __name__=="__main__":
   main()
