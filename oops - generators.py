def topten1():
    yield 1
    yield 2
    yield 3
    yield 4

a= topten1()
print(a)
for i in a:
    print(i)

'''
#topten perfect square

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

values = topten()

for i in values:
    print(i)
'''
