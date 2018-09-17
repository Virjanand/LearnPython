# Boolean values to evaluate conditions
x = 2
print(x == 2)
print(x == 3)
print(x < 3)
# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are 23 years old.")
    
if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
# The "in" operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
# Code blocks
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
    print("Another line of code.")
# Empty is false. Empty is empty string "", empty list [], number 0, false boolean variable: False
# The "is" operator checks if instances themselves match, not values
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)
# The "not" operator, inverts boolean expression
print(not False)
print((not False) == (False))

# Exercise, make eacht if statement true
number = 10
second_number = 10
first_array = []
second_array = [1,2,3]

if number < 15:
    print("1")
    
if not first_array:
    print("2")
    
if len(second_array) == 3:
    print("3")

if len(first_array) + len(second_array) == 3:
    print("4")
    
if not first_array and second_array[0] == 1:
    print("5")
    
if second_number:
    print("6")