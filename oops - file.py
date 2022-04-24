f=open('test1.txt','r')

'''
print(f)
print(f.readline(), end="")
print(f.readline())
'''
f1=open('abc', 'w')
f1.write("laptop")

f2=open('abc', 'a')
f2.write('mobile')

for i in f:
    #print(i, end="")
    f1.write(i)
    f2.write(i)

