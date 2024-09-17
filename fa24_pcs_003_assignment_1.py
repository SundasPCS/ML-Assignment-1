# -*- coding: utf-8 -*-
"""fa24-pcs-003_assignment 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OmolU6g4TlSz5y8HJelTl9pQOlWWHg5J
"""

# Question 1 onward
# Creating a dictionary
my_dict = {}

# Adding value pairs
my_dict['parrot'] = 2
my_dict['goat'] = 4
my_dict['spider'] = 8
my_dict['crab'] = 10

# Printing values
print(my_dict)

# Initialize counter
total_legs = 0

# Loop for dictionary items
for animal, legs in my_dict.items():
    print(f'{animal} has {legs} legs')
    total_legs += legs

# Print sum
print(f'Total legs: {total_legs}')

# list
nums = [3, 5, 7, 8, 12]
# Creating a new list
cubes = [num ** 3 for num in nums]
# Printing the cubes list
print(cubes)

# creating tuple
A = (3, 9, 4, [5, 6])

# changing the value
A[3][0] = 8

# Print changes
print(A)

# Delete tuple
del A

# Initialize
B = ('a', 'p', 'p', 'l', 'e')

# Count occurrences of 'p'
count_p = B.count('p')

# Print
print(f'Number of occurrences of \'p\': {count_p}')

index_l = B.index('l')

# Print the index
print(f'Index is \'l\': {index_l}')

# Question 2 onward
import numpy as np

# Define the matrix as a nested list
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Converting
array = np.array(a)

# Print
print(array)

import numpy as np

# Define the matrix as a NumPy array
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Use slicing
b = A[:2, 1:3]

# Print the resulting subarray
print(b)

# Create
C = np.zeros_like(A)

# Print
print(C)

# Define the vector z
z = np.array([1, 2, 3])

# Define
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
z = np.array([1, 0, 1])

# Create
C = np.zeros_like(A)


for i in range(A.shape[1]):
    C[:, i] = A[:, i] + z[i]

# Print matrix C
print(C)

import numpy as np

# Define matrix
X = np.array([[1, 2], [3, 4]])
Y = np.array([[5, 6], [7, 8]])
v = np.array([9, 10])

# Sum
sum_matrix = X + Y
print("Sum of matrices X and Y:")
print(sum_matrix)

# multiplication
product_matrix = X @ Y
print("\nProduct of matrices X and Y:")
print(product_matrix)

# Suare root
sqrt_Y = np.sqrt(Y)
print("\nElement-wise square root of matrix Y:")
print(sqrt_Y)

# Dot product
dot_product = X @ v
print("\nDot product of matrix X and vector v:")
print(dot_product)

# column vise sum
column_sums = np.sum(X, axis=0)
print("\nSum of each column of matrix X:")
print(column_sums)

# Question 3 onward
# Function for velocity
def Compute(distance, time):

    if time == 0:
        raise ValueError("Time cannot be zero.")
    velocity = distance / time
    return velocity


distance = 100
time = 20
velocity = Compute(distance, time)
print(f"Velocity: {velocity}")

# Create list of even numbers
even_num = [i for i in range(2, 13, 2)]
print("Even numbers up to 12:", even_num)

# Function to calculate the product of all entries in a list
def mult(numbers):

    product = 1
    for number in numbers:
        product *= number
    return product

# Calculate and print the product of the list 'even_num'
product_of_even_num = mult(even_num)
print("Product of all 'even_num':", product_of_even_num)

# Question 4 onward
import pandas as pd

# Create DataFrame using dictionary
data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

import pandas as pd


data = {
    'C1': [1, 2, 3, 5, 5],
    'C2': [6, 7, 5, 4, 8],
    'C3': [7, 9, 8, 6, 5],
    'C4': [7, 5, 2, 8, 8]
}

df = pd.DataFrame(data)

print("First two rows:")
print(df.head(2))

print("\nSecond column:")
print(df.iloc[:, 1])

df.rename(columns={'C3': 'B3'}, inplace=True)
print("\nDataFrame with 'C3' to 'B3':")
print(df)

df['Sum'] = None
print("\nDataFrame with new 'Sum' column added:")
print(df)

df['Sum'] = df.sum(axis=1)
print("\nDataFrame with 'Sum' column updated:")
print(df)

import pandas as pd

path="/content/sample_data/hello_sample.csv"
df=pd.read_csv(path)
# Print the complete DataFrame
print(df.to_string())

# Print only the bottom 2 records of the DataFrame
print(df.tail(2))

# Print information about the DataFrame
df.info()

# Print the shape (rows x columns) of the DataFrame
print(f'Shape of DataFrame: {df.shape[0]} rows x {df.shape[1]} columns')

#  Sort the DataFrame using the 'Weight' column
sorted_df = df.sort_values(by='Weight')
print(sorted_df)

# Check for null values and drop any rows with NaN values
print("Null values in DataFrame:\n", df.isnull().sum())
df_dropped = df.dropna()
print("DataFrame after dropping NaN values:\n", df_dropped)