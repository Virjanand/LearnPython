# list can contain any type, as many as you like
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1, 2, 3
for x in mylist:
    print(x)
    
# Exercise: number, string list and access second one
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

# this code should write out the filled arrays and the
# second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" %
    second_name)
