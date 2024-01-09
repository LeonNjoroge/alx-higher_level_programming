#!/usr/bin/python3
"""Adds command-line arguments to a Python list and saves them to a JSON file."""
import sys

if __name__ == "__main__":
    # Importing save_to_json_file and load_from_json_file functions
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Attempt to load existing items from the JSON file
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If the file is not found, initialize an empty list
        items = []
    
    # Extend the list with command-line arguments
    items.extend(sys.argv[1:])
    
    # Save the updated list to the JSON file
    save_to_json_file(items, "add_item.json")
