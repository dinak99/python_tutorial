# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

def x(a): return a + 10
def y(a, b): return a * b


def myfunc(n):
    return lambda a: a * n


print(x(5))
print(y(5, 6))
mydoubler = myfunc(2)
print(mydoubler(11))
