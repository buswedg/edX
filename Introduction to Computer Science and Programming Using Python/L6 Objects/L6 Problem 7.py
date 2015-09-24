def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

print testList


applyToEach(testList, abs)

print testList


def inc(a):
    return a+1
applyToEach(testList, inc)

print testList


def square(a):
    return a * a
applyToEach(testList, square)

print testList