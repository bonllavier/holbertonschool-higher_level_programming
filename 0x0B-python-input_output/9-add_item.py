#!/usr/bin/python3
import sys
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
"""
module 9-add_item
"""


new_list = []
filename = "add_item.json"
for item in range(len(sys.argv)):
    if item > 0:
        new_list.append(sys.argv[item])
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
    for iter2 in new_list:
        my_list.append(iter2)
    save_to_json_file(my_list, filename)
else:
    save_to_json_file(new_list, filename)
