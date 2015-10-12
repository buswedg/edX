
#Introduction to Computer Science and Programming Using Python

##Objects

###Problem 1


```python
x = (1, 2, (3, 'John', 4), 'Hi')
```


```python
print(x[0])
print(type(x[0]))
```

    1
    <type 'int'>
    


```python
print(x[2])
print(type(x[2]))
```

    (3, 'John', 4)
    <type 'tuple'>
    


```python
print(x[-1])
print(type(x[-1]))
```

    Hi
    <type 'str'>
    


```python
print(x[2][2])
print(type(x[2][2]))
```

    4
    <type 'int'>
    


```python
print(x[2][-1])
print(type(x[2][-1]))
```

    4
    <type 'int'>
    


```python
print(x[-1][-1])
print(type(x[-1][-1]))
```

    i
    <type 'str'>
    


```python
#print(x[-1][2])
#print(type(x[-1][2]))

#error
```


```python
print(x[0:1])
print(type(x[0:1]))
```

    (1,)
    <type 'tuple'>
    


```python
print(x[0:-1])
print(type(x[0:-1]))
```

    (1, 2, (3, 'John', 4))
    <type 'tuple'>
    


```python
print(len(x))
print(type(len(x)))
```

    4
    <type 'int'>
    


```python
print(2 in x)
print(type(2 in x))
```

    True
    <type 'bool'>
    


```python
print(3 in x)
print(type(3 in x))
```

    False
    <type 'bool'>
    


```python
#print(x[0] = 8)
#print(type(x[0] = 8))

#error
```

###Problem 2

Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple'). 


```python
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
```

###Problem 3


```python
x = [1, 2, [3, 'John', 4], 'Hi'] 
```


```python
print(x[0])
print(type(x[0]))
```

    1
    <type 'int'>
    


```python
print(x[2])
print(type(x[2]))
```

    [3, 'John', 4]
    <type 'list'>
    


```python
print(x[-1])
print(type(x[-1]))
```

    Hi
    <type 'str'>
    


```python
print(x[2][2])
print(type(x[2][2]))
```

    4
    <type 'int'>
    


```python
print(x[0:1])
print(type(x[0:1]))
```

    [1]
    <type 'list'>
    


```python
print(2 in x)
print(type(2 in x))
```

    True
    <type 'bool'>
    


```python
print(3 in x)
print(type(3 in x))
```

    False
    <type 'bool'>
    


```python
x[0] = 8
```


```python
print(x)
print(type(x))
```

    [8, 2, [3, 'John', 4], 'Hi']
    <type 'list'>
    

###Problem 4


```python
x = [1, 2, [3, 'John', 4], 'Hi']
```


```python
print(range(3))
print(type(range(3)))
```

    [0, 1, 2]
    <type 'list'>
    


```python
print(range(3, 10))
print(type(range(3, 10)))
```

    [3, 4, 5, 6, 7, 8, 9]
    <type 'list'>
    


```python
print(range(3, 10, 3))
print(type(range(3, 10, 3)))
```

    [3, 6, 9]
    <type 'list'>
    


```python
#print(range(3, 10.5, 0.5))
#print(type(range(3, 10.5, 0.5)))

#error
```


```python
print(range(10, 3))
print(type(range(10, 3)))
```

    []
    <type 'list'>
    


```python
print(range(10, 3, -1))
print(type(range(10, 3, -1)))
```

    [10, 9, 8, 7, 6, 5, 4]
    <type 'list'>
    


```python
print(range(len(x)))
print(type(range(len(x))))
```

    [0, 1, 2, 3]
    <type 'list'>
    


```python
print(sum(range(len(x))))
print(type(sum(range(len(x)))))
```

    6
    <type 'int'>
    

###Problem 5


```python
aList = range(1, 6)
bList = aList
aList[2] = 'hello'
```


```python
print(aList == bList)
print(type(aList == bList))
```

    True
    <type 'bool'>
    


```python
print(aList is bList)
print(type(aList is bList))
```

    True
    <type 'bool'>
    


```python
print(aList)
print(type(aList))
```

    [1, 2, 'hello', 4, 5]
    <type 'list'>
    


```python
print(bList)
print(type(bList))
```

    [1, 2, 'hello', 4, 5]
    <type 'list'>
    


```python
cList = range(6, 1, -1)
dList = []
for num in cList:
	dList.append(num)
```


```python
print(cList == dList)
print(type(cList == dList))
```

    True
    <type 'bool'>
    


```python
print(cList is dList)
print(type(cList is dList))
```

    False
    <type 'bool'>
    


```python
cList[2] = 20
```


```python
print(cList)
print(type(cList))
```

    [6, 5, 20, 3, 2]
    <type 'list'>
    


```python
print(dList)
print(type(dList))
```

    [6, 5, 4, 3, 2]
    <type 'list'>
    

###Problem 6


```python
listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']
```


```python
print(listA.sort)
print(type(listA.sort))
```

    <built-in method sort of list object at 0x000000000367AA88>
    <type 'builtin_function_or_method'>
    


```python
print(listA.sort())
print(type(listA.sort()))
```

    None
    <type 'NoneType'>
    


```python
print(listA)
print(type(listA))
```

    [0, 1, 3, 4]
    <type 'list'>
    


```python
print(listA.insert(0, 100))
print(type(listA.insert(0, 100)))
```

    None
    <type 'NoneType'>
    


```python
#print(listA.remove(3))
#print(type(listA.remove(3)))

#error
```


```python
print(listA.append(7))
print(type(listA.append(7)))
```

    None
    <type 'NoneType'>
    


```python
print(listA)
print(type(listA))
```

    [100, 100, 0, 1, 3, 4, 7, 7]
    <type 'list'>
    


```python
print(listA + listB)
print(type(listA + listB))
```

    [100, 100, 0, 1, 3, 4, 7, 7, 'x', 'z', 't', 'q']
    <type 'list'>
    


```python
listB.sort()
```


```python
print(listB.pop())
print(type(listB.pop()))
```

    z
    <type 'str'>
    


```python
print(listB.count('a'))
print(type(listB.count('a')))
```

    0
    <type 'int'>
    


```python
#print(listB.remove('a'))
#print(type(listB.remove('a')))

#error
```


```python
print(listA.extend([4, 1, 6, 3, 4]))
print(type(listA.extend([4, 1, 6, 3, 4])))
```

    None
    <type 'NoneType'>
    


```python
print(listA.count(4))
print(type(listA.count(4)))
```

    5
    <type 'int'>
    


```python
print(listA.index(1))
print(type(listA.index(1)))
```

    3
    <type 'int'>
    


```python
print(listA.pop(4))
print(type(listA.pop(4)))
```

    3
    <type 'int'>
    


```python
print(listA.reverse())
print(type(listA.reverse()))
```

    None
    <type 'NoneType'>
    


```python
print(listA)
print(type(listA))
```

    [100, 100, 0, 1, 7, 7, 4, 1, 6, 3, 4, 4, 1, 6, 3, 4]
    <type 'list'>
    

###Problem 7A

Assume that, testList = [1, -4, 8, -9]. Write a function so that testList returns: [5, -20, 40, -45]


```python
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

    return L
        
applyToEach(testList, abs)
```




    [1, 4, 8, 9]



###Problem 7B

Assume that, testList = [1, -4, 8, -9]. Write a function so that testList returns: [2, -3, 9, -8]


```python
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
    return L

def inc(a):
    return a+1

applyToEach(testList, inc)
```




    [2, -3, 9, -8]



###Problem 7C

Assume that, testList = [1, -4, 8, -9]. Write a function so that testList returns: [1, 16, 64, 81]


```python
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    
    return L
        
def square(a):
    return a * a

applyToEach(testList, square)
```




    [1, 16, 64, 81]



###Problem 8


```python
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
```


```python
applyEachTo([inc, square, halve, abs], -3)
```




    [-2, 9, -2, 3]




```python
applyEachTo([inc, square, halve, abs], 3.0)
```




    [4.0, 9.0, 1.5, 3.0]




```python
#applyEachTo([inc, max, int], -3)

#error
```

###Problem 9


```python
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'
```


```python
animals
```




    {'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}




```python
animals['c']
```




    'coati'




```python
#animals['donkey']

#error
```


```python
len(animals)
```




    4




```python
animals['a'] = 'anteater'
```


```python
animals['a']
```




    'anteater'




```python
len(animals['a'])
```




    8




```python
animals.has_key('baboon')
```




    False




```python
'donkey' in animals.values()
```




    True




```python
animals.has_key('b')
```




    True




```python
animals.keys()
```




    ['a', 'c', 'b', 'd']




```python
del animals['b']
len(animals)
```




    3




```python
animals.values()
```




    ['anteater', 'coati', 'donkey']



###Problem 10

Write a procedure, called howMany, which returns the sum of the number of values associated with a dictionary.


```python
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
```

###Problem 11

Write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.


```python
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
```
