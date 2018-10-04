# Sets
# Lists with no duplicate entries
print(set("my name is Eric and Eric is my name".split()))
a = set(["Jake", "John", "Eric"])
print(a)
b = set(["John", "Jill"])
print(b)

# Intersection of two sets
print(a.intersection(b))
print(b.intersection(a))

# Symmetric_difference to find out which members only in one set
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# Difference to find only in one set and not in other
print(a.difference(b))
print(b.difference(a))

# Union to list all in both sets
print(a.union(b))

# Exercise: print all from set a but not in set b
print(a.difference(b))