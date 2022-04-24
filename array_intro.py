from array import *
vals = array('i', [5,9,-8,4,2])

vals1 =array(vals.typecode, (a*a for a in vals))
for i in vals1:
    print(i, end=" ")

print()
i=0
while i <len(vals1):
    print(vals1[i])
    i+=1
