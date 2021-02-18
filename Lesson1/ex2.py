import math


def f12(x):
    if x < -20:
        return math.log10((x ** 5) + x) + math.cos(math.tan(x) - math.log10(x))
    if x < 37:
        return 31 * x * x + 32 * (x ** 8)
    if x < 65:
        return x ** 4 - abs(x)
    if x < 104:
        return math.tan(x ** 4) - math.log(x)
    return x ** 7 / 64 - math.sin(x)



#print(foo(75))
#print(foo(27))

