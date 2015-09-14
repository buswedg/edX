def a(x, y, z):
     if x:
         return y
     else:
         return z


def b(q, r):
    return a(q>r, q, r)



print(type(a(False, 2, 3)))
print(a(False, 2, 3))

print(type(b(3, 2)))
print(b(3, 2))

print(type(a(3>2, a, b)))
print(a(3>2, a, b))

print(type(b(a, b)))
print(b(a, b))