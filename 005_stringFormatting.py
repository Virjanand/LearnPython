# String formatting with argument specifiers
name = "John"
print("Hello, %s!" % name)
# Use two or more argument specifiers
name = "Jane"
age = 23
print("%s is %d years old." % (name, age))

# objects have "repr" method to format it as string
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# Exercise: write Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f"
print(format_string % data)