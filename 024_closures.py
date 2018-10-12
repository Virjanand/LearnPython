# Closures
# Nested function can use variables (read-only).

def transmit_to_space(message):
  "This is the enclosing function"
  def data_transmitter():
    "The nested function"
    print(message)
    
  data_transmitter()
  
print(transmit_to_space("Test message"))

# With the "nonlocal" keyword they can be modified.

def print_msg(number):
  def printer():
    "Here we are using the nonlocal keyword"
    nonlocal number
    number = 3
    print(number)
  printer()
  print(number)
  
print_msg(9)

# Return the function object instead of calling it
def transmit_to_moon(message):
  "This is the enclosing function"
  def data_transmitter():
    "The nested function"
    print(message)
  return data_transmitter
  
fun2 = transmit_to_moon("Burn the sun!")
fun2()

# Used for avoiding global variables and some form of data hiding.

# Exercise: make a nested loop and a python closure to get
# multiple multiplication functions using closure

# your code goes here
def multiplier_of(multiplier_number):
  def multiplier(number):
    product = multiplier_number * number
    print(product)
    return product
  return multiplier

multiplywith5 = multiplier_of(5)
multiplywith5(9)