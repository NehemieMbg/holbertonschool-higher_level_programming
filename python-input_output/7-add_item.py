#!/usr/bin/python3
"""7. Load, add, save"""
"""Script that adds all arguments to a Python list,
and save them to a file"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    fileContent = load_from_json_file("add_item.json")
except FileNotFoundError:
    fileContent = []
save_to_json_file(fileContent + (argv[1:]), "add_item.json")
