import math


def f13(x):
    step_1 = 0
    step_2 = 0
    for i in range(x+1):
        step_1 += (math.sin((36 * i) - (i * i)) + (math.exp(1) ** i))
        step_2 += (i - (i * i))

    step_1 /= 67
    step_2 *= 46

    return step_1 + step_2


#print(foo(77))
#print(foo(12))