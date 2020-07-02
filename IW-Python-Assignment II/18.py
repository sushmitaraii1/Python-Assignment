# 18. Find a package in the Python standard library for dealing with JSON. Import the library module and inspect the
# attributes of the module. Use the help function to learn more about how to use the module. Serialize a dictionary
# mapping 'name' to your name and 'age' to your age, to a JSON string. Deserialize the JSON back into Python.

import json
# help(json)


# Serialize a dictionary
dict_info = {'name':'Sushmita', 'age':21}
with open("data_file.json", "w") as write_file:
    json.dump(dict_info, write_file)

# Deserialize the JSON back into Python
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)
