def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x*x + b*x + c



print(evalQuadratic(-9.48, -3.17, 4.96, 9.28))
print(evalQuadratic(-1.1, 1.12, 8.22, 1.5))
print(evalQuadratic(8.69, -6.81, -3.02, 3.87))
print(evalQuadratic(8.41, 0.64, -7.88, -2.07))
print(evalQuadratic(9.67, -1.75, 0.01, -3.57))