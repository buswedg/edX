
# coding: utf-8

# #Introduction to Computer Science and Programming Using Python

# ##Functions

# ###Problem 1

# In[1]:

def a(x):
   '''
   x: int or float.
   '''
   return x + 1


# In[2]:

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0


# In[3]:

def c(x, y):
   '''
   x: int or float.
   y: int or float.
   '''
   return x + y


# In[4]:

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y


# In[5]:

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z


# In[6]:

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2


# In[7]:

print(type(a(6)))
print(a(6))


# In[8]:

print(type(a(-5.3)))
print(a(-5.3))


# In[9]:

print(type(a(a(a(6)))))
print(a(a(a(6))))


# In[10]:

print(type(c(a(1), b(1))))
print(c(a(1), b(1)))


# In[11]:

print(type(d('apple', 11.1)))
print(d('apple', 11.1))


# In[12]:

print(type(e(a(3), b(4), c(3, 4))))
print(e(a(3), b(4), c(3, 4)))


# In[13]:

print(type(f))
print(f)


# ###Problem 2

# In[14]:

def a(x, y, z):
    if x:
        return y
    else:
        return z

def b(q, r):
    return a(q>r, q, r)


# In[15]:

print(type(a(False, 2, 3)))
print(a(False, 2, 3))


# In[16]:

print(type(b(3, 2)))
print(b(3, 2))


# In[17]:

print(type(a(3>2, a, b)))
print(a(3>2, a, b))


# In[18]:

print(type(b(a, b)))
print(b(a, b))


# ###Problem 3

# Write a Python function, square, that takes in one number and returns the square of that number. 

# In[19]:

def square(x):
    '''
    x: int or float.
    '''
    return x*x


# ###Problem 4

# Write a Python function, evalQuadratic(a, b, c, x), that returns the value of the quadratic a⋅x2+b⋅x+c.

# In[ ]:

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x*x + b*x + c


# ###Problem 5

# Write a Python function, clip(lo, x, hi) that returns lo if x is less than lo; hi if x is greater than hi; and x otherwise. For this problem, you can assume that lo < hi.
# 
# Don't use any conditional statements for this problem. Instead, use the built in Python functions min and max. 

# In[ ]:

def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(x, lo), hi)


# ###Problem 6

# In[ ]:

a = 10
def f(x):
    return x + a
a = 3

print(type(f(1)))
print(f(1))


# In[ ]:

x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)

print(type(g(x)))
print(g(x))


# ###Problem 7

# In[ ]:

def foo(x):
    def bar(x):
        return x + 1
    return bar(x * 2)

foo(3)


# In[ ]:

def foo (x):
    def bar (z):
        return z + x
    return bar(3)

foo(2)


# ###Problem 8

# Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power. 

# In[ ]:

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


# ###Problem 9

# Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.
# 
# You should use the % (mod) operator, not if. 

# In[ ]:

def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return (x % 2 == 1)

