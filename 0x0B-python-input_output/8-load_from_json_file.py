#!/usr/bin/python3
def load_from_json_file(filename):
    """
    load from json file
    """
    import json
    with open(filename, "r") as f:
        data = json.load(f)
    return data
