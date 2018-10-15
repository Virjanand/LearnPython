# Decorators
# Modify callable objects like functions, methods, or classes
# 2 ways to define:
# @_decorator
# def functions(arg):
#    return "value"

# or

# def function(arg):
#     return "value"
# function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions

# Decorator is a function that takes another function
# and returns another function
def repeater(old_function):
    def new_function(*args, **kwds): # See learnpython.org/page/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwds) # we run the old function
        old_function(*args, **kwds) # we do it twice
    return new_function # we have to return the new_function, or it wouldn't reassign it to the value
    
@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 3)

# Change output
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function
    
# Change input
def double_Ii(old_function):
    def new_function(arg): # only works if the old function has one argument
        return old_function(arg * 2) # modify the argument passed
    return new_function
    
# Do checking
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function
    
# Multiply the output by a variable amount
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15

# Exercise: take one argument type and return decorator
# that checks input is correct type, if it is wrong print
# "Bad Type". Use isinstance(object, type_of_object) or type(object)
def type_check(correct_type):
    def check(old_function):
      def new_function(arg):
        if (isinstance(arg, correct_type)):
          return old_function(arg)
        else:
          print("Bad type")
      return new_function
    return check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])