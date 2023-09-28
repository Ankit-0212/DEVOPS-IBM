def outer(x):
    def inner(y):
        return x+y
    return inner

myFunc = outer(3)

print(outer(23)(23))
print(myFunc(2))
