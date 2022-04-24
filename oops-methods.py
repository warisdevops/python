''' instance(accessors, mutators), class, static methods'''

class student:
    school = 'telusko'

    def __init__(self, m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

#accessors to get variable values using methods
    def getm1(self):
        return self.m1
#mutators to get variable values using methods
    def setm1(self, value):
         self.m1=value
    @classmethod
    def big(cls):
        return cls.school
    @staticmethod
    def info():
        print('hello this is static method, not instance/class variables', 'welcome to our school')

a=student(1,2,3)
b=student(4,5,6)
c=student(7,8,9)

print(student.big())
student.info()

'''
a.m1=10
print(a.m1)

print(a.setm1(100))
print(a.getm1())'''




