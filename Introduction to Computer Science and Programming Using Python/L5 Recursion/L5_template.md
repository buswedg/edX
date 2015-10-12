
#Introduction to Computer Science and Programming Using Python

##Recursion

###Problem 1

Write an iterative function iterPower(base, exp) that calculates the exponential baseexp by simply using successive multiplication. For example, iterPower(base, exp) should compute baseexp by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer ≥ 0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed. 


```python
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result
```

###Problem 2

Write a function recurPower(base, exp) which computes baseexp by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; exp will be an integer ≥0. It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed. 


```python
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp <= 0:
        return 1

    return base * recurPower(base, exp - 1)
```

###Problem 3

Write a procedure recurPowerNew which recursively computes exponentials using the idea:

- base^exp = (base^2)^exp/2, if exp>0 and exp is even
- base^exp = base . base^exp-1, if exp>0 and exp is odd
- base^exp = 1, if exp = 0


```python
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp <= 0:
        return 1
    
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)
```

###Problem 4

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder.

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.


```python
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
    
    return testValue
```

###Problem 5

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers: 

- If b = 0, then the answer is a 
- Otherwise, gcd(a, b) is the same as gcd(b, a % b) 

Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer. 


```python
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    
    return gcdRecur(b, a % b)
```

###Problem 6

Although Python provides a built-in function for computing the length of a string, we can write our own.

Write an iterative function, lenIter, which computes the length of an input argument (a string), by counting up the number of characters in the string.


```python
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    count = 0
    for char in aStr:
        count += 1
    
    return count
```

###Problem 7

Write a recursive function, lenRecur, which computes the length of an input argument (a string), by counting up the number of characters in the string. 


```python
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0

    return 1 + lenRecur(aStr[1:])
```

###Problem 8

We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order. 

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value. 


```python
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
   
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
   
    if len(aStr) == 1:
        return aStr == char
   
    midIndex = len(aStr)/2
    midChar = aStr[midIndex]
    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])
```

###Problem 9

A semordnilap is a word or a phrase that spells a different word when backwards ("semordnilap" is a semordnilap of "palindromes"). Here are some examples:

- nametag / gateman
- dog / god
- live / evil
- desserts / stressed

Write a recursive program, semordnilap, that takes in two words and says if they are semordnilap.


```python
def semordnilapWrapper(str1, str2):
    if len(str1) == 1 or len(str2) == 1:
        return False

    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False

    if len(str1) == 1:
        return str1 == str2

    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False
```
