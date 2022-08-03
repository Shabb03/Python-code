#!/usr/bin/env python3

print("Enter a number, enter nothing to end")

def game():
   n = input()
   while n != "":
      if int(n) % 3 == 0 and int(n) % 5 == 0:
         print("fizzbuzz")
      elif int(n) % 3 == 0:
         print("fizz")
      elif int(n) % 5 == 0:
         print("buzz")
      else:
         print(n)
      n = input()

if __name__=="__main__":
   game()
