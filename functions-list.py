'''''function to return even and odd numbers - pass input as list'''

n = int(input("user enter number of values in list"))
list1= []
for i in range(n):
    a= int(input("enter elements"))
    list1.append(a)
print(list1)
''' count even and odd numbers .....................................................'''

def count(list1):
    e=0
    o=0
    for i in list1:
        if i%2==0:
            e+=1
        else:
            o+=1
    return e,o

e1,o1 = count(list1)
print(e1,o1)
print("total even numbers {} and total odd numbers {}".format(e1,o1))


'''
def sort_even_odd(l1):
    for i in l1:
        if i%2 ==0:
            return even
'''
