'''
Working with NumPy arrays.
'''
import numpy as np

#creating numpy arrays

#create 1D and 2D arrays using array function
arr1d = np.array([1,2])
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)

#create array using arange function
arr_ar = np.arange(1,100,9)

#create array using linspace function
arr_lp = np.linspace(10,11,10)

#create array using logspace function
arr_logp = np.logspace(10,15,10)

#create array using various functions
arr_zeros = np.zeros((2,3))
arr_ones = np.ones((3,2))
arr_empty = np.empty((2,4))
arr_identity = np.identity(3)

#accessing array elements
print('arr1d =',arr1d)
print('arr2d =')
for row in arr2d:
    print(row)
print('arr_ar =',arr_ar)
print('arr_lp =',arr_lp,' having size of',arr_lp.size)
print('arr_logp =',arr_logp,' having size of',arr_logp.size)
print('arr_zeros =\n',arr_zeros)
print('arr_ones =\n',arr_ones)
print('arr_empty =\n',arr_empty)
print('arr_identity =\n',arr_identity)

#performing array operations
print('\nPerforming Array Operations:')
print('Addition of 2D arrays\n',arr2d + arr_identity)
print('Substraction of 2D arrays\n',arr2d - arr_identity)
print('Multiplication of 2D arrays\n',arr2d * arr_identity)
print('Matrix Multiplication of 2D arrays\n',arr2d @ arr_identity)
print('Transpose of 2D arrays\n',arr2d.transpose())

#performing slice operations
print('Elements of Second Row and First 2 Columns',arr2d[1,:2])
print('Elements of Last Row and Second Column onwards',arr2d[-1,1:])
print(arr2d[arr1d])

#performing reshape on arrays