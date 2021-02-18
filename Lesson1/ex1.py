import math


def f11(x):
    step_1 = ((math.sin((36 * x) - (x * x)) + math.exp(1) ** x) / (72 * (x ** 6) + math.log10(x)))
    step_2 = (math.sqrt((36 * (x ** 7) + x ** 5) / (x ** 5 - math.cos(x))))
    step_3 = ((x ** 8 + 79 * (x ** 5) + 84) / (x ** 5 + x))
    return step_1 - step_2 - step_3


#print(foo(17))
#print(foo(20))