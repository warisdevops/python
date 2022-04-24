from numpy import *
arr1= array([1,2,3,4,5])

#aliasing
#arr2= arr1
#print(arr2)
#print(id(arr1))
#print(id(arr2))

#shallow copy
#arr2=arr1.view()
#arr1[1]=7
#print(arr1)
#print(arr2)
#print(id(arr1))
#print(id(arr2))

#deep copy
arr2=arr1.copy()
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

