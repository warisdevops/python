from numpy import *

arr1= array([[1,2,3] , [4,5,6] ])
print(arr1)
#use methods below
print("dimension is " , arr1.ndim)
print("shape is ", arr1.shape)
print(arr1.size)

arr2= arr1.flatten()
print(arr2)

arr3=array([[1,2,3,6,2,9], [4,5,6,7,5,3]])
print(arr3)
print(arr3.reshape(4,3))
print(arr3.reshape(2,2,3))

#matrices
arr4 =array([[1,2,3,6] , [4,5,6,7] ])
m = matrix(arr4)
print(m)

m1=matrix('1 2 3; 6 4 5; 1 6 7')
print(m1)
m2= matrix('1 2 3; 6 8 5; 2 6 7')
m3 = m1*m2
print(m3)
print(m3.max())


