# Exception handling
# try/except block
def do_stuff_with_number(n):
  print(n)

the_list = (1, 2, 3, 4, 5)

for i in range(20):
  try:
    do_stuff_with_number(the_list[i])
  except IndexError: # Raised when accessing a non
                     # -existing index of a list
    do_stuff_with_number(0)
    
# Exercise
# Handle all the exceptions!
#Setup
actor = {"name": "John Cleese", "rank": "awesome"}

#Function to modify, should return the last name of the actor - think back to previous lessons for how to get it
def get_last_name():
  try:
    return actor["last_name"]
  except KeyError:
    return "Cleese"

#Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())