# Dictionaries are like arrays, but with key values as index
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
# Alternative way to initialize
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
# Iterating over dictionaries, order not kept
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
# Removing a value
del phonebook["John"]
print(phonebook)
# Alternative way to remove a value
phonebook.pop("Jack")
print(phonebook)

# Exercise: add "Jake to phonebook with 938273443 and
#           remove Jill
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
# write your code here
phonebook["Jake"] = 938273443
phonebook.pop("Jill")
# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")