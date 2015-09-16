def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Initialize a variable to hold our final count
    count = 0

    # Iterate over each character in the string, counting each one
    for char in aStr:
        count += 1
    return count

print (lenIter("test"))