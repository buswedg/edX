def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(x, lo), hi)



print(clip(-3.99, -4.64, -0.3))
print(clip(-3.46, 2.41, -2.5))
print(clip(-6.82, 0.8, -6.13))
print(clip(-0.91, -1.08, 2.72))
print(clip(-9.83, -5.04, -4.58))
print(clip(3.69, -3.1, 9.15))
print(clip(-4.16, -4.41, 4.99))
print(clip(-9.35, -7.21, 6.11))
print(clip(-9.73, -2.05, 1.76))
print(clip(2.44, 1.97, 3.39))