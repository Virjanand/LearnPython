# Multiple function arguments
# Normally
def myfunction(first, second, third):
  print(first)
  print(second)
  print(third)

myfunction("one", "two", "three")

# Variable number of arguments
def foo(first, second, third, *therest):
  print("First: %s" % first)
  print("Second: %s" % second)
  print("Third: %s" % third)
  print("And all the rest... %s" % list(therest))
  
foo("one", "two", "three", "four", "five", "six")

# Function arguments by keyword, so order of argument does not matter.
def bar(first, second, third, **options):
  if options.get("action") == "sum":
    print("The sum is: %d" %(first + second + third))
    
  if options.get("number") == "first":
    return first
    
result = bar(1, 2, 3, action = "sum", number = 'first')
print("Result: %d" % result )

# Exercise: foo must return amount of extra arguments received
#   bar must return true if the argument with keyword magicnumber
#   is 7 and false otherwise
def foo(a, b, c, *rest):
  return len(list(rest))

def bar(a, b, c, **rest):
   if rest.get("magicnumber") == 7:
     return True
   return False
 
if foo(1, 2, 3, 4) == 1:
  print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
  print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
  print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
  print("Awesome!")