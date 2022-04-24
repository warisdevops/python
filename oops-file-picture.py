f=open('IMG_1323.PNG', 'rb')
f1=open('mypic.PNG', 'wb')

for i in f:
    f1.write(i)
