a = [1,2,3,4,5]

# iterator is an object that manages an iteration
# list iterator object
i = iter(a)
print(i)

# next provide next element in the underlying series
print(next(i))
print(next(i))
print(next(i))
print(next(i))

def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, b+a


i = fib()
for j in range(50):
    print(next(i))
