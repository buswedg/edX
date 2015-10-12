
# coding: utf-8

# #Introduction to Computer Science and Programming Using Python

# ##Objects

# ###Problem 1

# In[1]:

x = (1, 2, (3, 'John', 4), 'Hi')


# In[2]:

print(x[0])
print(type(x[0]))


# In[3]:

print(x[2])
print(type(x[2]))


# In[4]:

print(x[-1])
print(type(x[-1]))


# In[5]:

print(x[2][2])
print(type(x[2][2]))


# In[6]:

print(x[2][-1])
print(type(x[2][-1]))


# In[7]:

print(x[-1][-1])
print(type(x[-1][-1]))


# In[8]:

#print(x[-1][2])
#print(type(x[-1][2]))

#error


# In[9]:

print(x[0:1])
print(type(x[0:1]))


# In[10]:

print(x[0:-1])
print(type(x[0:-1]))


# In[11]:

print(len(x))
print(type(len(x)))


# In[12]:

print(2 in x)
print(type(2 in x))


# In[13]:

print(3 in x)
print(type(3 in x))


# In[14]:

#print(x[0] = 8)
#print(type(x[0] = 8))

#error


# ###Problem 2

# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple'). 

# In[15]:

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    rTup = ()
    index = 0

    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup


# ###Problem 3

# In[16]:

x = [1, 2, [3, 'John', 4], 'Hi'] 


# In[17]:

print(x[0])
print(type(x[0]))


# In[18]:

print(x[2])
print(type(x[2]))


# In[19]:

print(x[-1])
print(type(x[-1]))


# In[20]:

print(x[2][2])
print(type(x[2][2]))


# In[21]:

print(x[0:1])
print(type(x[0:1]))


# In[22]:

print(2 in x)
print(type(2 in x))


# In[23]:

print(3 in x)
print(type(3 in x))


# In[24]:

x[0] = 8


# In[25]:

print(x)
print(type(x))


# ###Problem 4

# In[26]:

x = [1, 2, [3, 'John', 4], 'Hi']


# In[27]:

print(range(3))
print(type(range(3)))


# In[28]:

print(range(3, 10))
print(type(range(3, 10)))


# In[29]:

print(range(3, 10, 3))
print(type(range(3, 10, 3)))


# In[30]:

#print(range(3, 10.5, 0.5))
#print(type(range(3, 10.5, 0.5)))

#error


# In[31]:

print(range(10, 3))
print(type(range(10, 3)))


# In[32]:

print(range(10, 3, -1))
print(type(range(10, 3, -1)))


# In[33]:

print(range(len(x)))
print(type(range(len(x))))


# In[34]:

print(sum(range(len(x))))
print(type(sum(range(len(x)))))


# ###Problem 5

# In[35]:

aList = range(1, 6)
bList = aList
aList[2] = 'hello'


# In[36]:

print(aList == bList)
print(type(aList == bList))


# In[37]:

print(aList is bList)
print(type(aList is bList))


# In[38]:

print(aList)
print(type(aList))


# In[39]:

print(bList)
print(type(bList))


# In[40]:

cList = range(6, 1, -1)
dList = []
for num in cList:
	dList.append(num)


# In[41]:

print(cList == dList)
print(type(cList == dList))


# In[42]:

print(cList is dList)
print(type(cList is dList))


# In[43]:

cList[2] = 20


# In[44]:

print(cList)
print(type(cList))


# In[45]:

print(dList)
print(type(dList))


# ###Problem 6

# In[46]:

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']


# In[47]:

print(listA.sort)
print(type(listA.sort))


# In[48]:

print(listA.sort())
print(type(listA.sort()))


# In[49]:

print(listA)
print(type(listA))


# In[50]:

print(listA.insert(0, 100))
print(type(listA.insert(0, 100)))


# In[51]:

#print(listA.remove(3))
#print(type(listA.remove(3)))

#error


# In[52]:

print(listA.append(7))
print(type(listA.append(7)))


# In[53]:

print(listA)
print(type(listA))


# In[54]:

print(listA + listB)
print(type(listA + listB))


# In[55]:

listB.sort()


# In[56]:

print(listB.pop())
print(type(listB.pop()))


# In[57]:

print(listB.count('a'))
print(type(listB.count('a')))


# In[58]:

#print(listB.remove('a'))
#print(type(listB.remove('a')))

#error


# In[59]:

print(listA.extend([4, 1, 6, 3, 4]))
print(type(listA.extend([4, 1, 6, 3, 4])))


# In[60]:

print(listA.count(4))
print(type(listA.count(4)))


# In[61]:

print(listA.index(1))
print(type(listA.index(1)))


# In[62]:

print(listA.pop(4))
print(type(listA.pop(4)))


# In[63]:

print(listA.reverse())
print(type(listA.reverse()))


# In[64]:

print(listA)
print(type(listA))


# ###Problem 7A

# Assume that, testList = [1, -4, 8, -9]. Write a function so that testList returns: [5, -20, 40, -45]

# In[65]:

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

    return L
        
applyToEach(testList, abs)


# ###Problem 7B

# Assume that, testList = [1, -4, 8, -9]. Write a function so that testList returns: [2, -3, 9, -8]

# In[66]:

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
    return L

def inc(a):
    return a+1

applyToEach(testList, inc)


# ###Problem 7C

# Assume that, testList = [1, -4, 8, -9]. Write a function so that testList returns: [1, 16, 64, 81]

# In[67]:

testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
    return L
        
def square(a):
    return a * a

applyToEach(testList, square)


# ###Problem 8

# In[68]:

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1


# In[69]:

applyEachTo([inc, square, halve, abs], -3)


# In[70]:

applyEachTo([inc, square, halve, abs], 3.0)


# In[71]:

#applyEachTo([inc, max, int], -3)

#error


# ###Problem 9

# In[72]:

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'


# In[73]:

animals


# In[74]:

animals['c']


# In[75]:

#animals['donkey']

#error


# In[76]:

len(animals)


# In[77]:

animals['a'] = 'anteater'


# In[78]:

animals['a']


# In[79]:

len(animals['a'])


# In[80]:

animals.has_key('baboon')


# In[81]:

'donkey' in animals.values()


# In[82]:

animals.has_key('b')


# In[83]:

animals.keys()


# In[84]:

del animals['b']
len(animals)


# In[85]:

animals.values()


# ###Problem 10

# Write a procedure, called howMany, which returns the sum of the number of values associated with a dictionary.

# In[86]:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        result += len(value)
    
    return result


# ###Problem 11

# Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

# In[87]:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result

