#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
	# Check if thr first name is a string
	if type(first_name) is not str:
		raise TypeError("{:s} must be a string".format("first_name"))
	# Check if the last name is a string
	if type(last_name) is not str:
		raise TypeError("{:s} must be a string".format("last_name"))
	# If the first and last name are strings
	else:
		print("My name is {:s} {:s}".format(first_name, last_name))
