# Numpy Arrays
# Alternative to Python lists
# Fast, easy to work with, calculations accross entire arrays

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# Element wise calculations
# Very fast and computationally efficient
# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
print(bmi > 25)

# Print only those observations above 23
print(bmi[bmi > 25])

# Exercise convert list to Numpy array, then convert weights from kg to pounds
# Finally print weights in pounds (1 kg = 2.2 pounds)
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = 2.2 * np_weight_kg

# Print out np_weight_lbs
print(np_weight_lbs)