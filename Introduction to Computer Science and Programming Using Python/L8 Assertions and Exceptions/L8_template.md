
#Introduction to Computer Science and Programming Using Python

##Assertions and Exceptions

###Problem 2


```python
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
```


```python
FancyDivide([0, 2, 4], 1)
```

    1
    0
    


```python
FancyDivide([0, 2, 4], 4)
```

    -1
    0
    


```python
#FancyDivide([0, 2, 4], 0)

#error
```


```python
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
```


```python
FancyDivide([0, 2, 4], 1)
```

    1
    0
    


```python
FancyDivide([0, 2, 4], 4)
```

    1
    0
    0
    


```python
FancyDivide([0, 2, 4], 0)
```

    -2
    0
    


```python
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
```


```python
FancyDivide([0, 2, 4], 1)
```

    1
    0
    


```python
FancyDivide([0, 2, 4], 4)
```

    1
    0
    0
    


```python
FancyDivide([0, 2, 4], 0)
```

    0
    -2
    


```python
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
```


```python
FancyDivide([0, 2, 4], 0)
```

    integer division or modulo by zero
    


```python
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
```


```python
FancyDivide([0, 2, 4], 0)
```

    0
    

###Problem 3

When dividing by 0, FancyDivide should return a list with all 0 elements. Any other error cases should still raise exceptions.


```python
def SimpleDivide(item, denom):
    try:
        return item / denom

    except ZeroDivisionError, e:
        return 0
```
