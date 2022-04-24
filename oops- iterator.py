'''
a = [7,8,9,5]
it= iter(a)
print(it)

for i in range(4):
    print(next(it)) '''

# create your own iterator
# create top 10 values

class topten:
    def __init__(self):
        self.n =1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <=10:
            val =self.n
            self.n+=1
            return val
        else:
            raise StopIteration

values = topten()
for i in values:
    print(i)


