
def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f



x= 4
result = fact(x)
print(result)