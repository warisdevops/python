class student():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        x=self.m1+other.m1
        y=self.m2+other.m2
        z=student(x,y)
        return z
    def __gt__(self, other):
        x1=self.m1+self.m1
        y1=other.m1+other.m2
        if x1>y1:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

a=student(100,2000)
b=student(60,65)
c=a+b

if a>b:
    print('a wins')
else:
    print('b wins')

print(c.m1)

test=9
print(test) #0r
print(test.__str__())

print(a)
print(b)




