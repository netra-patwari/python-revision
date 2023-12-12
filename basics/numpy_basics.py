import numpy as np

# #a = np.array([1,2,3,4])
# b = np.array([[1.0, 2.0, 3.0], [2.0, 3.4, 35.6]])

# # print(a)
# # print(b)

# # print(b.ndim) #number of dimension

# # print(a.shape)
# # print(b.shape) #rows and cols

# a = np.array([1,2,3,4] , dtype='int16') #updation of dtype
# # print(a.dtype) #datatype
# # print(a.itemsize) #byte size int16 = 2bytes

# print(a.size) #total size


#! Accessing/Changing specific elements, rows, columns, etc



a = np.array([[1,2,3,4,5] , [5,4,3,2,1]])

# Get a specific element [r, c]
# print(a[1,1])

# Get a specific row
# print(a[0,:])


# Get specific coloumn
# print(a[:,1])


# Getting a Little more fancy [startindex:endindex:stepsize
# print(a[0,1 :-1 : 2])


# !Initializing Different Types of Arrays

# All zero matrix
# d =np.zeros((2,3,4,3))
# print(d)

# All one matrix
# d =np.ones((2,3) ,  dtype='int32')
# print(d)


# Any other number
# d =np.full((2,3,3) , 99)
# print(d)


# # 
# b = np.full_like(a,2)
# print(b)


# Random decimal number
# e = np.random.rand(2,3,3)
# print(e)

# e = np.random.random_sample(a.shape)
# print(e)

# random int
# e = np.random.randint(72, size=(3,3)) #start value(0--default) , endvalue , size
# print(e)

# Identity matrix
# e = np.identity(3) # 1 -> in principal axis 
# print(e)


# Repeat an array
# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3,axis=0)
# print(r1)


# !COPYING ARRAY
# arr = np.array([1,2,3,4])
# brr = arr.copy()
# print(brr)

# ! MATHEMATICS
# arr = np.array([1,2,3,4])
# brr = arr.copy()

# print(arr+2)
# print(arr-2)
# print(arr*2)
# print(arr/2)
# print(arr ** 2)
# print(np.sin(arr))
# print(arr + brr)

# !LOAD DATA FROM FILE  
filedata = np.genfromtxt('basics/data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

print(filedata > 40)