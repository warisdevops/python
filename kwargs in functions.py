def person(name, **data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person('navin', age=28, city='mumbai', phone=9885673475)



