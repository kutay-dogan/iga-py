import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

zeros_arr = np.zeros((3, 3))       # 3x3 matrix of zeros
ones_arr = np.ones((2, 4))         # 2x4 matrix of ones
range_arr = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8] (start, stop, step)
space_arr = np.linspace(0, 1, 5)   # [0., 0.25, 0.5, 0.75, 1.] (5 evenly spaced numbers)
identity_arr = np.identity(3)      # 3x3 identity matrix
eye_arr = np.eye(3,4)

print("Shape:", arr_2d.shape)      # Output: (2, 3)
print("Dimensions:", arr_2d.ndim)  # Output: 2


a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)  # [11, 22, 33]
print(a * b)  # [10, 40, 90]
print(a ** 2) # [1, 4, 9] (Squaring every element)
print(eye_arr)
print(identity_arr)

# Create a 1D array of 12 numbers and reshape it into a 3x4 matrix
grid = np.arange(12).reshape((3, 4)) # use -1 
"""
[[ 0,  1,  2,  3],
 [ 4,  5,  6,  7],
 [ 8,  9, 10, 11]]
"""

# Slicing: Get the first two rows and the last two columns
sub_grid = grid[:2, 2:] 
"""
[[ 2,  3],
 [ 6,  7]]
"""

grid = np.array([[1, 2], [3, 4]])

# Option A: ravel() - The fast way
flat_view = grid.ravel() 
# Returns a "view" of the original array. Modifying flat_view changes 'grid'. Fast and memory efficient.

# Option B: flatten() - The safe way
flat_copy = grid.flatten() 
# Returns a completely new copy. Modifying flat_copy does NOT change 'grid'.

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])

# Swap rows and columns
transposed = matrix.T
"""
[[1, 4],
 [2, 5],
 [3, 6]]
"""

data = np.array([15, -3, 22, 8, -5, 42])

# Create a boolean mask where elements are greater than 10
mask = data > 10 
# Output: [ True, False,  True, False, False,  True]

# Apply the mask to get only the filtered values
filtered_data = data[mask] 
# Output: [15, 22, 42]

# Alternatively, do it in one line:
positive_data = data[data > 0]

# 3x3 matrix of 1s
matrix = np.ones((3, 3))
row_vector = np.array([0, 1, 2])

# The 1D row_vector is broadcast across all 3 rows of the matrix
result = matrix + row_vector 
"""
[[1., 2., 3.],
 [1., 2., 3.],
 [1., 2., 3.]]
"""


scores = np.array([85, 42, 90, 33, 78])

# np.where(condition, value_if_true, value_if_false)
grades = np.where(scores >= 50, 'Pass', 'Fail')
# Output: ['Pass' 'Fail' 'Pass' 'Fail' 'Pass']


# TASK 1
# Create a 1D NumPy array containing even numbers from 0 up to (but not including) 40. 
# Then, reshape this array into a 2D grid that has exactly 4 rows, letting NumPy calculate the number of columns automatically.
# HINT: Use np.arange() 

# TASK 2
# Using the grid you created in Task 1, use slicing to extract a sub_grid containing only the first 2 rows and the last 2 columns. 
# Then, use broadcasting to add a 1D row vector [100, 200] to every row of your new sub_grid.

# TASK 3: Safe Flattening and Boolean Masking
# ake your original grid from Task 1 and safely flatten it into a completely new 1D array (a copy, not a view). 
# Once flattened, create a boolean mask to filter the array so that it only retains values strictly greater than 15.

# TASK 4
# Using the filtered data from Task 3, use np.where to evaluate the numbers. 
# If a number is greater than 25, replace it with the string 'Pass'; otherwise, replace it with 'Fail'.

# TASK 5
# Create a 3x4 matrix of ones and swap its rows and columns so it becomes a 4x3 matrix.
