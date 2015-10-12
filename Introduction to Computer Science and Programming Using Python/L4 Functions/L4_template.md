
#Introduction to Computer Science and Programming Using Python

##Functions

###Problem 1


```python
def a(x):
   '''
   x: int or float.
   '''
   return x + 1
```


```python
def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
```


```python
def c(x, y):
   '''
   x: int or float.
   y: int or float.
   '''
   return x + y
```


```python
def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y
```


```python
def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z
```


```python
def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
```


```python
print(type(a(6)))
print(a(6))
```

    <type 'int'>
    7
    


```python
print(type(a(-5.3)))
print(a(-5.3))
```

    <type 'float'>
    -4.3
    


```python
print(type(a(a(a(6)))))
print(a(a(a(6))))
```

    <type 'int'>
    9
    


```python
print(type(c(a(1), b(1))))
print(c(a(1), b(1)))
```

    <type 'float'>
    4.0
    


```python
print(type(d('apple', 11.1)))
print(d('apple', 11.1))
```

    <type 'bool'>
    True
    


```python
print(type(e(a(3), b(4), c(3, 4))))
print(e(a(3), b(4), c(3, 4)))
```

    <type 'bool'>
    False
    


```python
print(type(f))
print(f)
```

    <type 'function'>
    <function f at 0x0000000003680748>
    

###Problem 2


```python
def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)
```


```python
print(type(a(False, 2, 3)))
print(a(False, 2, 3))
```

    <type 'int'>
    3
    


```python
print(type(b(3, 2)))
print(b(3, 2))
```

    <type 'int'>
    3
    


```python
print(type(a(3>2, a, b)))
print(a(3>2, a, b))
```

    <type 'function'>
    <function a at 0x0000000003680AC8>
    


```python
print(type(b(a, b)))
print(b(a, b))
```

    <type 'function'>
    <function b at 0x0000000003680B38>
    

###Problem 3

Write a Python function, square, that takes in one number and returns the square of that number. 


```python
def square(x):
    '''
    x: int or float.
    '''
    return x*x
```

###Problem 4

Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a⋅x2+b⋅x+c.


```python
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x*x + b*x + c
```

###Problem 5

Write a Python function, clip(lo, x, hi) that returns lo if x is less than lo; hi if x is greater than hi; and x otherwise. For this problem, you can assume that lo < hi.

Don't use any conditional statements for this problem. Instead, use the built in Python functions min and max. 


```python
def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(x, lo), hi)
```

###Problem 6


```python
a = 10
def f(x):
    return x + a
a = 3

print(type(f(1)))
print(f(1))
```


```python
x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)

print(type(g(x)))
print(g(x))
```

###Problem 7


```python
def foo(x):
    def bar(x):
        return x + 1
    return bar(x * 2)

foo(3)
```


```python
def foo (x):
    def bar (z):
        return z + x
    return bar(3)

foo(2)
```

###Problem 8

Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power. 


```python
def square(x):
    '''
    x: int or float.
    '''
    return x*x

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))
```

###Problem 9

Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.

You should use the % (mod) operator, not if. 


```python
def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return (x % 2 == 1)
```
