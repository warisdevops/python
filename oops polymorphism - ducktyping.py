''' polymorphism ---> duck typing/ operator overloading/ method overloading/ method overriding '''

'''duck typing'''

class pycharm:
    def method(self):
        print('commands in pycharm')

class sublime:
    def method(self):
        print('command in sublime')


class laptop:
    def code(self, ide):
        ide.method()

ide=pycharm()
a=laptop()
a.code(ide)

