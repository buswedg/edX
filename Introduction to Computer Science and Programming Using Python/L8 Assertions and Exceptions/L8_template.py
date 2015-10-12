
# coding: utf-8

# #Introduction to Computer Science and Programming Using Python

# ##Assertions and Exceptions

# ###Problem 2

# In[1]:

def FancyDivide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
    finally:
        print "0"


# In[2]:

FancyDivide([0, 2, 4], 1)


# In[3]:

FancyDivide([0, 2, 4], 4)


# In[4]:

#FancyDivide([0, 2, 4], 0)

#error


# In[5]:

def FancyDivide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        FancyDivide(numbers, len(numbers) - 1)
    except ZeroDivisionError, e:
        print "-2"
    else:
        print "1"
    finally:
        print "0"


# In[6]:

FancyDivide([0, 2, 4], 1)


# In[7]:

FancyDivide([0, 2, 4], 4)


# In[8]:

FancyDivide([0, 2, 4], 0)


# In[9]:

def FancyDivide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError, e:
            FancyDivide(numbers, len(numbers) - 1)
        else:
            print "1"
        finally:
            print "0"
    except ZeroDivisionError, e:
        print "-2"


# In[10]:

FancyDivide([0, 2, 4], 1)


# In[11]:

FancyDivide([0, 2, 4], 4)


# In[12]:

FancyDivide([0, 2, 4], 0)


# In[13]:

def FancyDivide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception, e:
        print e


# In[14]:

FancyDivide([0, 2, 4], 0)


# In[15]:

def FancyDivide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e


# In[16]:

FancyDivide([0, 2, 4], 0)


# ###Problem 3

# When dividing by 0, FancyDivide should return a list with all 0 elements. Any other error cases should still raise exceptions.

# In[17]:

def SimpleDivide(item, denom):
    try:
        return item / denom

    except ZeroDivisionError, e:
        return 0

