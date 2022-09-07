#!/usr/bin/python3
# prints ASCII alphabets exept the e and q not followed by a new line
for letter in range(97, 123):
	if letter == 113 or letter == 101:
		continue
	print("{}".format(chr(letter)), end='')
