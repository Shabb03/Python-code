#!/usr/bin/env python3

import sys

print("Symbols are: Add +, Subtract -, Multiply x, Divide /")

def calculator():
   symbols = ['+', '-', 'x', '/']
   problem = [i for i in sys.argv[1:]]
   mord = []
   count = 0

   for j in range(len(problem)):
      if problem[j] == symbols[2]:
         mord.append(int(problem[j-1]) * int(problem[j+1]))
      elif problem[j] == symbols[3]:
         mord.append(int(problem[j-1]) / int(problem[j+1]))
      elif problem[j] == symbols[0]:
         mord.append(symbols[0])
      elif problem[j] == symbols[1]:
         mord.append(symbols[1])
      elif (j == 0) and (problem[j+1] in symbols[0:2]):
         mord.append(int(problem[j]))
      elif (j == len(problem) - 1) and (problem[j-1] in symbols[0:2]):
         mord.append(int(problem[j]))
      elif (2 <= j <= (len(problem) - 3)) and (problem[j-1] in symbols[0:2] and problem[j+1] in symbols[0:2]):
         mord.append(int(problem[j]))

   if len(mord) > 0:
      count += mord[0]
      for k in range(1, len(mord) - 1):
         if mord[k] == symbols[0]:
            print(mord[k+1])
            count += mord[k+1]
         elif mord[k] == symbols[1]:
            count -= mord[k+1]
   else:
      for k in range(len(problem)):
         if problem[k] == symbols[0]:
            count += float(problem[k-1]) + float(problem[k+1])
         elif problem[k] == symbols[1]:
            count += float(problem[k-1]) - float(problem[k+1])

   print(float(count))

if __name__=="__main__":
   calculator()
