#!/usr/bin/python3
# prints the result of the addition of all arguments
if __name__ == "__main__":
    from sys import argv

result = 0
for index in argv[1:]:
    result += int(index)
print(result)
