# Serialization
# Decode and encode json
# String: used to pass data to another program
# Object datastructure: use with python methods
import json

# Load JSON back to a data structure
# takes string and turns it back into json object

# dumps: encode data structure to JSON
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json.loads(json_string))

# cPickle does the same
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# Exercise: print JSON string with key-value pair "Me":800 added
# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here
    salaries = json.loads(salaries_json)
    salaries.update({name: salary})
    salaries_json = json.dumps(salaries)
    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])