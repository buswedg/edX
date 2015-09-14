a = 10
def f(x):
    return x + a
a = 3


x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)



print(type(f(1)))
print(f(1))

print(type(g(x)))
print(g(x))