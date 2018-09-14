# integer
myint = 7
print(myint)

# float
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# double vs single quotes
mystring = "Don't worry about apostrophes"
print(mystring)

# operators on numbers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# multiple assignments
a, b = 3, 4
print(a, b)

# mixin numbers and strings not supported
one = 1
two = 2
hello = "hello"
#print(one + two + hello)

# exercise: string, float and int
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)