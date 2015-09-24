x = [1, 2, [3, 'John', 4], 'Hi']

print(range(3))
print(type(range(3)))

print(range(3, 10))
print(type(range(3, 10)))

print(range(3, 10, 3))
print(type(range(3, 10, 3)))

#print(range(3, 10.5, 0.5))
#print(type(range(3, 10.5, 0.5)))

print(range(10, 3))
print(type(range(10, 3)))

print(range(10, 3, -1))
print(type(range(10, 3, -1)))

print(range(len(x)))
print(type(range(len(x))))

print(sum(range(len(x))))
print(type(sum(range(len(x)))))