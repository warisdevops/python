#compile time error ==> syntax error
#logical errors ==> code compile and output done, but output is incorrect(real logic missing)
# runtime error ==> no compile/logical error ==> user input ==> need to tell user some suggestions to input correctly
# runtime error, think that the run time shouldnt stop even after providing suggestions

a=5

b=0

try:
    print('resource open')
    print(a/b)
    k = int(input('enter a number'))
    print(k)

    #print('resource closed')
# only when try has error, except will be executed, if not will move on to run other code
except ZeroDivisionError as e:
    print('hey you cannot divide using zero', e)
except ValueError as e:
    print('invalid input, expected interger, string entered', e)
except Exception as e:
    print("exception error bro- all exceptions", e)
    #print('resource closed in exception')

finally:
    print('resource closed in finally')
print('Bye')

# if you open a file you need to close that file
