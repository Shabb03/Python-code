#!/usr/bin/env python3

import random

print("Enter a number between 0 and 100")

def game():
   random_n = random.randint(0, 100)
   n = input()
   while n != "":
      if int(n) == random_n:
         print("Correct!")
         break
      elif int(n) > random_n:
         print("Number is too high")
      elif int(n) < random_n:
         print("Number is too low")
      n = input()

if __name__=="__main__":
   game()
