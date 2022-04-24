''' instance and class(static)'''

class car:
    wheels = 4
    def __init__(self):
        self.milage=10
        self.company='bmw'

a=car()
b=car()

a.milage=5
car.wheels = 2
print(a.milage, a.company, a.wheels)
print(b.milage, b.company, b.wheels)

