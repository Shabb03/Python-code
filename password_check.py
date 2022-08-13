#!/usr/bin/env python3

word = input("Enter Password:  ")
security = [0, 0, 0, 0]
strength = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
print(word)

if len(word) < 5:
    print(strength[0])
elif len(word) > 4 and len(word) < 10:
    print(strength[1])
else:
    for c in word:
        if c.islower():
            security[0] = 1
        elif c.isupper():
            security[1] = 1
        elif c.isdigit():
            security[2] = 1
        else:
            security[3] = 1

    print(strength[sum(security)])