#!/usr/bin/python3
# prints all possible different combinations of two digit
for i in range(8):
    for j in range(i, 10):
        if i != j:
            print("{:d}{:d}, ".format(i, j), end='')
print(89)
