#!/usr/bin/python3
# Prints all number from 0 to 98
for i in range(100):
    if i == 99:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
