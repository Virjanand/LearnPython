# List comprehensions
# Create a list based on another list
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
  if word != "the":
    word_lengths.append(len(word))
print(words)
print(word_lengths)

# using word comprehensions:
word_lengths_compreh = [len(word) for word in words if word != "the"]
print(word_lengths_compreh)

# Exercise: create newlist out of list "numbers" with only 
# positive numbers as integers
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number > 0]
print(newlist)