#!/usr/bin/python3
"""From JSON string to Object"""
import json

def from_json_string(my_str):
	"""Returns an object Python data structure"""
	return(json.loads(my_str))
