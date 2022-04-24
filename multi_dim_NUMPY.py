from numpy import *
#arr = array([1,2,3,-4,5.0], float)
arr= linspace(0,10,5)
print(arr.dtype)
print(arr)

b= arange(1,10,1)
print(b)

c= logspace(1,10,5)
print(c)
print('%.2f' %c[1])

d= zeros(10)
print(d)

e=ones(10)
print(e)

f=ones(10, int)
print(f)