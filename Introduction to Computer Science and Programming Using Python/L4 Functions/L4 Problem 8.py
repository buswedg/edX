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



print(fourthPower(8.07))
print(fourthPower(-0.34))
print(fourthPower(-6.05))
print(fourthPower(2.04))
print(fourthPower(-3.02))