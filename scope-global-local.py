a=10

def something():
    a=15
    print("inside", a)

something()
print("outside", a)

'''2nd code..............................................................................'''
print("2nd code output below")
a=10
b=35

def something():
    global a,b
    b=20
    a=15
    print("inside", a)

something()
print("outside", a)

'''3rd code...............................................................................'''
print("3rd code output below")
a=10
print(id(a))

def something():
    a=15
    x=globals()['a']
    print("x inside", a)
    print(x)
    print(id(x))
    print("inside a", a)
something()

print("outside a", a)
