aList = range(1, 6)
bList = aList
aList[2] = 'hello'

print(aList == bList)
print(type(aList == bList))

print(aList is bList)
print(type(aList is bList))

print(aList)
print(type(aList))

print(bList)
print(type(bList))


cList = range(6, 1, -1)
dList = []
for num in cList:
	dList.append(num)

print(cList == dList)
print(type(cList == dList))

print(cList is dList)
print(type(cList is dList))


cList[2] = 20

print(cList)
print(type(cList))

print(dList)
print(type(dList))