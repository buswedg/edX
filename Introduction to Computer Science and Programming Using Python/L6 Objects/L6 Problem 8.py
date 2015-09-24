def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a

	
def halve(a):
    return a/2

	
def inc(a):
    return a+1


applyEachTo([inc, square, halve, abs], -3)

applyEachTo([inc, square, halve, abs], 3.0)

applyEachTo([inc, max, int], -3)