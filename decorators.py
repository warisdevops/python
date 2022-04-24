def div(a,b):
    print(a/b)

def function1(function2):
    def inner(x,y):
        if x<y:
            x,y =y,x
            return function2(x,y)
    return inner



div1= function1(div)

div1(2,100000)
