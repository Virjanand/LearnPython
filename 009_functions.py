# Functions are blocks of code
#block_head:
#    1st block line
#    2nd block line

# Functions are defined using def func_name
def my_function():
    print("Hello from my function!")
# Arguments
def my_function_with_args(username, greeting):
    print("Hello, %s, from my function! I wish you %s" %
    (username, greeting))
# Return values
def sum_two_numbers(a, b):
    return a + b
# Call function
my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1, 2)
print(x)
# Exercise use existing function and create own
#  1. list_benefits() returns list of strings: 
#    "More organized code", 
#    "More readable code", 
#    "Easier code reuse", 
#    "Allowing programmers to share and connect code together"
#  2. build_sentence(info) returns string with info at start and
#    " is a benefit of functions!" at the endswith
# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", 
    "More readable code", 
    "Easier code reuse", 
    "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()