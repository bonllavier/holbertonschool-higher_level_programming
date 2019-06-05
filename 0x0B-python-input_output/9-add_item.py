#!/usr/bin/python3
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
import sys
new_list = []
filename = "add_item.json"
for item in range(len(sys.argv)):
    if item > 0:
        new_list.append(sys.argv[item])
#print(new_list)
save_to_json_file(new_list, filename)
