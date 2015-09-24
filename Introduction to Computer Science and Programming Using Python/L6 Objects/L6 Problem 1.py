x = (1, 2, (3, 'John', 4), 'Hi')

print(x[0])
print(type(x[0]))

print(x[2])
print(type(x[2]))

print(x[-1])
print(type(x[-1]))

print(x[2][2])
print(type(x[2][2]))

print(x[2][-1])
print(type(x[2][-1]))

print(x[-1][-1])
print(type(x[-1][-1]))

#print(x[-1][2])
#print(type(x[-1][2]))

print(x[0:1])
print(type(x[0:1]))

print(x[0:-1])
print(type(x[0:-1]))

print(len(x))
print(type(len(x)))

print(2 in x)
print(type(2 in x))

print(3 in x)
print(type(3 in x))

#print(x[0] = 8)
#print(type(x[0] = 8))