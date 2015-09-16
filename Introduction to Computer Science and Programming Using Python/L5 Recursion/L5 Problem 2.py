def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Otherwise, exp must be > 0, so return
    #  base* base^(exp-1). This is the recursive case.
    return base * recurPower(base, exp - 1)

print (recurPower(2, 2))