# list = [10,2,333]
# list.append([1])
# print(list)
# print(min(list))

# import array as arr
# from array import *

# val =  array('i' , [5,9,7,8])
# val.reverse()
# print(val[2])


# from array import *

# arr = array('i' , [])

# n = int(input("Enter the lenght of array : "))

# for i in range(n):
#     try:
#         x = int(input("Enter next value : "))
#         arr.append(x)
#     except:
#       print('An exception occurred. Input must be a number')
    
    
# print(arr)

import numpy as np

#a = np.array([1,2,3,4])
b = np.array([[1.0, 2.0, 3.0], [2.0, 3.4, 35.6]])

# print(a)
# print(b)

# print(b.ndim) #number of dimension

# print(a.shape)
# print(b.shape) #rows and cols

a = np.array([1,2,3,4] , dtype='int16') #updation of dtype
# print(a.dtype) #datatype
# print(a.itemsize) #byte size int16 = 2bytes

print(a.size)
