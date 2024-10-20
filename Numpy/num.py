import numpy as np

# np_array = np.array([0,1,2,3,4,5,6,7,8,9])

# print(np_array) 

# ls_num = [0,1,2,3,4,5,6,7,8,9]

# print(ls_num[0::2])

# broadcasting arrays of same shape //Example1
a = np.array([1.0,2.0,3.0])

b = np.array([2.0, 2.0, 2.0])

c = a * b

print('c',c)

# when an array and a vector meets //Example2

d = np.array([1.0,2.0,3.0])

e = 2.0

f = d * e

print('f',f)

# Computation in Example1 is more effecient because broadcasting moves less memory during the multi[plication operation


# comparing numpy array and python list based on slicing

# python list
py_list = [1, 2, 4, 5, 6]

sliced_py_list = py_list[1:4]
sliced_py_list[0] = 99

print("og list", py_list)
print("sliced list", sliced_py_list)

# numpy array

arr = np.array(py_list)

sliced_arr = arr[1:4]

sliced_arr[0] = 99

print('og arr', arr)
print('sliced arr', sliced_arr)

# ARRAY DIMENSIONS

# array with 2 diemnsions
arr_dim = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# accessing an element witthin the multidimensional array
print("3 position element in the second array",arr_dim[1, 3])

# ATTRIBUTES


# getting the number of dimension in an array
print("dimension",arr_dim.ndim)

# getting the shape
print("shape", arr_dim.shape)

# getting the size
print("size", arr_dim.size)

# array data type
print("data type", arr_dim.dtype)

# CREATING AN ARRAY

# array of zeros
zeros = np.zeros(2)
print("zeros",zeros)

# array of ones
ones = np.ones(2)
print("ones",ones)

# empty arrays
empty = np.empty(2)
print("empty",empty)

# creating array using a range of elements
arr_range = np.arange(4)
print("array in range",arr_range)

# creating via spaced intervals
arr_range_interval = np.arange(2, 9, 2)
print("range in interval",arr_range_interval)

# linespace
linespace = np.linspace(0, 10, num=5)
print("linespace",linespace)

# specifying data type
d_type = np.ones(2, dtype=np.int64)
print("data type",d_type)

# Adding, removing and sorting elements

# sortiang
sort_arr = np.sort(arr)
print("sorted array",sort_arr)

# concantenate array
concat = np.concatenate((a,b))
print("concat",concat)

# RESHAPING AN ARRAY

arr_to_reshape = np.arange(6)
reshape = arr_to_reshape.reshape(3,2)
print("reshape",reshape)

# with optional parameters
reshape_param = np.reshape(arr_to_reshape, shape=(1, 6), order='C')
print("reshape with optional parameter", reshape_param)

# CONVERTING 1D ARRAY TO 2D

# using np.newaxis
# this is for inserting along row vector
row_new_axis = arr[np.newaxis, :]

# this is for inserting along column vector
col_new_axis = arr[:, np.newaxis]

# Using np.expand_dims
# add axis at index postion 1
ind_1 = np.expand_dims(arr, axis=1)

# add axis at index position 0
ind_0 = np.expand_dims(arr, axis=0)


# SLICING A NUMPY ARRAY

data = np.array([1, 2, 3])

data[1]
data[0:2]
data[1:]
data[-2:]

# printing values in array based on certain conditions

# print elements less than 5
less_than_5 = arr_dim[arr_dim < 5 ]
print("less than 5",less_than_5)

# print elements from 5 upwards
five_upwards = arr_dim[arr_dim >= 5 ]
print("5 upwards", five_upwards)

# satisfying two conditions
two_conditions = arr_dim[(arr_dim > 2) & (arr_dim < 11)]
print("two conditions",two_conditions)

# boolean values can also be returned if the elements meet the specified conditions
five_up = (arr_dim > 5) | (arr_dim == 5)
print(five_up)

# You can use nonzero() to print indices of certain elements
none_zero = np.nonzero(arr_dim < 5)
print(none_zero)
# a tupele of arrays will be returned one for each dimension, the first array represent the row indices where the values are
# found, while the second one represents the column indices where the values are found.

# CREATING ARRAY FROM EXISTING ARRAYS

# By slicing
arr_exists = np.array([1,2,3,4,5,6,7,8])

sliced_arr_exists = arr_exists[3:]
print("new sliced array",sliced_arr_exists)

# stacking two arrays vertically or horizontally
a_one = np.array([[1, 1], [2,2]])
a_two = np.array([[3, 3], [4,4]])

# stacking vertically
stacked_array_vert = np.vstack((a_one,a_two))
print("new vertically stacked array",stacked_array_vert)

# stack horizaontally
stacked_array_hor = np.hstack((a_one,a_two))
print("new horizontally stacked array", stacked_array_hor)

# using hsplit
arr_to_hsplit = np.arange(1, 25).reshape(2, 12)

# split to three equally shaped array
hsplit_array_three = np.hsplit(arr_to_hsplit, 3)
print("hsplit array", hsplit_array_three)

# splitting after the third and fourth column
hsplit_array_three_four = np.hsplit(arr_to_hsplit,(3,4))

# view is just like when we tried to modify data in normal slicing and how it modified the original array.
# we use copy(), if we want to create a deep copy, an entirely different one from the original
arr_copy = arr_to_hsplit.copy()
print("copied arry", arr_copy)

# sum
arr_to_sum = np.array([[1,1], [2,2]])

# sum across the axis of rows(in the column)
sumed_ovr_row = arr_to_sum.sum(axis=0)
print("sum across the axis of rows(in the column)",sumed_ovr_row)

# sum across the axis of columns(in the row)
sumed_ovr_col = arr_to_sum.sum(axis=1)
print("sum across the axis of column(in the row)",sumed_ovr_col)

# FIND MAX AND MIN
data = np.array([1.0,2.0])

# get max
max_val = data.max()
print("max",max_val)

# get min
min_val = data.min()
print("min",min_val)


# UNIQUE ITEMS AND COUNT

arr_data = np.array([11,22,33,44,55,11,11,66,66,11,22,55,88,77,99,99,77])

# getting unique numbers
unique_val = np.unique(arr_data)
print("unique value",unique_val)

# getting indices of unique array
unique_val,unique_indices = np.unique(arr_data, return_index=True)
print("The indices of the unique elements",unique_indices)

# can also return count..based on the number of times they occur
unique = np.unique(arr_data, return_counts=True, return_index=True)
print("return counts of unique elements",unique[2])

# finding unique element in a 2D array, it is good to note that if you do not indicate the 
# axis in the unique method it will return a flatten array
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])

# flatten array
flatten_unique_arr = np.unique(a_2d)
print("flatten 2d array", flatten_unique_arr)

# get unique rows(but each value in each column are unique)
unique_row_val = np.unique(a_2d, axis=0)
print("unique row values",unique_row_val)

# get unique columns(but each value in each rows are unique)
unique_col_val = np.unique(a_2d, axis=1)
print("unique col values",unique_col_val)

# TRANSPOSING AND RESHAPING MATRICES
arr_to_transpose = np.arange(6).reshape((2, 3))

# transpose using .transpose()
arr_trans = arr_to_transpose.transpose()
print(arr_to_transpose)
print("transpose array using .transpose()",arr_trans)

# transpose using .T
arr_T = arr_to_transpose.T
print("transpose array using T",arr_T)

# REVERSING AN ARRAY

arr_to_reverse = np.array([1,2,3,4,5,6,7,8])

# reverse a 1D array
reverse_1D = np.flip(arr_to_reverse)
print("reverse 1D",reverse_1D)

# Reverse a 2D array
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reverse_2D = np.flip(arr_2d)
print("Reverse 2D", reverse_2D)

# Reverse 2D array row
reverse_row_2D = np.flip(arr_2d, axis=0)
print("reverse row",reverse_row_2D)

# Reverse 2D array column
reverse_col_2D = np.flip(arr_2d, axis=1)
print("reverse col",reverse_col_2D)

# You can decide to reverse the content of just one row or one column

# reverse content of the row at index position 1
reverse_one_row = np.flip(arr_2d[1])
print("reversed one row", reverse_one_row)

# reverse content of column at index position 1
reverse_one_col = np.flip(arr_2d[:,1])
print("reverse one column", reverse_one_col)

# FLATTEN AN ARRAY

# creates an array different from the original
flatten_arr = arr_2d.flatten()
print("flatten using flatten",flatten_arr)

# creates an array that refrences the original array
flatten_ravel_arr = arr_2d.ravel()
print("flatten using ravel()", flatten_ravel_arr)









