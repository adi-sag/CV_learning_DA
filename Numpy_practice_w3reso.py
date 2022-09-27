# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:31:40 2020
@author: Sagale
"""
#%%Write a NumPy program to get the numpy version and show numpy build configuration.
import numpy as np
print(np.__version__)
print(np.show_config())

#%%Write a NumPy program to get help on the add function.
import numpy as np
print(np.info(np.add))
#%%
#Write a NumPy program to test whether none of the elements of a given array is zero.
import numpy as np
x = np.array([1,False, 2, 3, 4])
print("Original array: ", x )
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
x = np.array([7, 1, 2, 1])
print("Original array:" ,x )
print("Test if none of the elements of the said array is zero:")
print(np.all(x))

#%%
#Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))
#%%
#Write a NumPy program to test element-wise for complex number, real number of a given array. Also test whether a given number is a scalar type or not.
import numpy as np
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(3.1)) # isscalar function wont be able to recognise and loop through all the elments in the list.
print(np.isscalar([3.1])) # here the the value given to isscalar function is list. hence it returns False.
#%%Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.
import numpy as np
x = np.array([3, 5])
y = np.array([2, 5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")
print(np.less_equal(x, y))

#%%Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
import numpy as np
X = np.array([1, 7, 13, 105])
print("Original array:")
print(X)
print("Size of the memory occupied by the said array:")
print("%d bytes" % (X.size * X.itemsize))
#%%
#Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
import numpy as np
rand_num = np.random.normal(0,1,15)    #https://www.w3schools.com/python/numpy_random_normal.asp
print("15 random numbers from a standard normal distribution:")
print(rand_num)
#%%Write a NumPy program to create a 3X4 array using and iterate over it.

import numpy as np
a = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
# np.nditer() function : used to iterate over values in array 
for x in np.nditer(a):
  print(x , end = " ")
#%% Reverse an array 
import numpy as np
import numpy as np
x = np.arange(12, 38)
print("Original array:")
print(x)
print("Reverse array:")
x = x[::-1]
print(x)
#%% 
import numpy as np
x = np.ones((5,5))
print("Original array:")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)

#%%Write a NumPy program to create a 8x8 matrix and fill it with a checkerboard pattern.
import numpy as np

x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
# here slicing works as [start:end:step]
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)
#%%Write a NumPy program to append values to the end of an array.
import numpy as np
x = [10, 20, 30]
print("Original array:")
print(x)
x = np.append(x, [[40, 50, 60], [70, 80, 90]])
print("After append values to the end of the array:")
print(x)
#%%Write a NumPy program to convert a list and tuple into arrays.
import numpy as np
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(my_list))
my_tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(my_tuple))
#%%
###########################################################################
################## NUMPY LINEAR ALGEBRA ###################################
###########################################################################
#%% matrix multiplication 
import numpy as np
p = [[1, 5], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p, q)
result2 = np.dot(q, p)
print("Result of the said matrix multiplication:")
print(result1)
print(result2)
#%%  Write a NumPy program to compute the outer product of two given vectors. 
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result = np.outer(p, q)
print("Outer product of the said two vectors:")
print(result)
#%%
###########################################################################
############################# NUMPY RANDOM ################################
###########################################################################
#%% Write a NumPy program to shuffle numbers between 0 and 10 (inclusive).
import numpy as np
x = np.arange(10)
np.random.shuffle(x)
print(x)
print("Same result using permutation():")
print(np.random.permutation(x))
print(np.random.permutation(x))
print(np.random.permutation(x))
#%% testing of above code
arr = np.arange(9).reshape((3, 3))
print(np.random.permutation(arr))

#%% Write a NumPy program to normalize a 3x3 random matrix.
import numpy as np
x= np.random.random((3,3))
print("Original Array:")
print(x)
xmax, xmin = x.max(), x.min()
x = (x - xmin)/(xmax - xmin)
print("After normalization:")
print(x)

#%% Write a NumPy program to check two random arrays are equal or not.
import numpy as np
x = np.random.randint(0,2,6)
print("First array:")
print(x)
y = np.random.randint(0,2,6)
print("Second array:")
print(y)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(x, y)
print(array_equal)
#%% Write a NumPy program to find the most frequent value in an array. 
import numpy as np
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
#bincount command return the frequency of occurence of numbers at its repective indexes. 
print(np.bincount(x))
print(np.bincount(x).argmax())
#%%