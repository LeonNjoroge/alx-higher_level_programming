#!/usr/bin/python3
"""Adds command-line arguments to a list and saves them to a JSON file."""
import sys

if __name__ == "__main__":
    # Importing save_to_json_file and load_from_json_file functions
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    try:
        # Attempt to load existing items from the JSON file
        val = load_from_json("add_item.json")
    except FileNotFoundError:
        # If the file is not found, initialize an empty list
        val = []

    # Extend the list with command-line arguments
    val.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(val, "add_item.json")
