av= 10
x=int(input("how many candies "))

i=1
while i<=x:
    if i>av:
        print('dispatched', i-1, 'machine out of candies')
        break
    print("take candies ")
    i+=1

print('bye')