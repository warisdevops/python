class computer:
    def __init__(self):
        self.name='navin'
        self.age=28
    def update(self):
        self.age=30
    def compare(self, other):
        if self.age==other.age:
            return True
        else:
            return False



a= computer()
b=computer()
a.age=30

print(a.compare(b))

print(a.name, b.name, a.age, b.age)

