# Partial functions
# Derive a function to a function with fewer parameters and fixed values
from functools import partial

def multiply(x, y):
  return x * y
  
# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))

# values will be replaced from left

# Exercise: replace first 3 variables, so that it returns 60
# with only one input parameter
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
partial_func = partial(func, 5, 10, 3)
print(partial_func(4))