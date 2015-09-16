def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)

print (gcdRecur(2, 2))