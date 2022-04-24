from array import *
arr = array('i', [])

#how many values user needs
x= int(input("how many values you need"))
for i in range(x):
    a = int(input("pls enter values"))
    arr.append(a)

print(arr)

cust = int(input('enter matching element to get the index position'))
i=0
for element in arr:
    if element == cust:
        print(i)
        break
    i+=1

print(arr.index(element))



