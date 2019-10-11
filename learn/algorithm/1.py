def f(i):
    return i*2


def g(i):
    return i*3


ss = sum(f(i) + g(i) for i in range(1, 10))
print(ss)