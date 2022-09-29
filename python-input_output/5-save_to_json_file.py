#!/usr/bin/python3
"""5. Save Object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a, Object to a text file, usint JSON representation"""
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(my_obj, f)
