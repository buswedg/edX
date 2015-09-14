str1 = 'exterminate!'
str2 = 'number one - the larch'



print(str1.upper)
print(type(str1.upper))

print(str1.upper())
print(type(str1.upper()))

print(str1)
print(type(str1))

print(str1.isupper())
print(type(str1.isupper()))

print(str1.islower())
print(type(str1.islower()))

print(str2.capitalize())
print(type(str2.capitalize()))

print(str2.swapcase())
print(type(str2.swapcase()))

print(str1.index('e'))
print(type(str1.index('e')))

print(str2.index('n'))
print(type(str2.index('n')))

print(str2.find('n'))
print(type(str2.find('n')))

print(str2.index('!'))
print(type(str2.index('!')))

print(str2.find('!'))
print(type(str2.find('!')))

print(str1.count('e'))
print(type(str1.count('e')))

str1 = str1.replace('e', '*')
print(str1)
print(type(str1))

print(str2.replace('one', 'seven'))
print(type(str2.replace('one', 'seven')))