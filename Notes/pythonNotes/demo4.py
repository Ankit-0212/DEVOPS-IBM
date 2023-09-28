# varargs and kwargs

def myFunc(*args):
    print(type(args))

myFunc(  1,3,4,3,'Python ')

def myFunc1(**kwargs):
    for key,value in kwargs.items():
        print("key : ",key,"|","value : ",value)




myFunc1(name = 'abcd',company = 'IBM')