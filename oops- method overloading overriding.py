#method overLOADING 2 same method names inside same class but with different arguments
class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    '''def sum(self, a=None, b=None, c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        return s'''
    '''
    def sum(self, a, *b):
        s=0
        print(a)
        print(b)
        for i in range(b):
            s+=i
        return s+a

x=student(10,20)

print(x.sum(1,2,3,4))'''

#-----------------------------------------------------------------------
#METHOD OVERRIDING -class  inheritance as example with two classes, each having same methogd name

class A:
    def show(self):
        print('in A SHOW')

class B(A):
    def show(self):
        print('in B SHOW')
    pass

a=B()
a.show()
