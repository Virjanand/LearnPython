# Strings are text
astring = "Hello world!"
astring2 = "Hello world!"
# For single quotes use double quotes
print("single quotes are ' '")
print(len(astring))
# Location of first occurrence of letter
print(astring.index("o"))
# Count number of occurrences of letter
print(astring.count("l"))
# Slice excluding character at last number 
# (without final number until end, -3 from end)
print(astring[3:7])
# Skipping characters
print(astring[3:7:2])
# Reverse string
print(astring[::-1])
# Upper- and lowercase
print(astring.upper())
print(astring.lower())
# Determine string starts or ends with something
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# Split string based on character
print(astring.split(" "))

# Exercise: Fix code to print correct information
s = "Hey thera! what should this string be?"
# Length should be 20
s = s[0:20]
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))