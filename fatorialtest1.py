

from functools import reduce


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]


evens = list(filter(lambda n : n%2==0, list1))

print(evens)


#doubles = list(map(funtion1, sequence))
doubles = list(map(lambda n: n*2, evens))
print(doubles)

#reduces = list(reduce(function2, sequence))

reduce_sum = reduce(lambda a,b: a+b, doubles)
print(reduce_sum)