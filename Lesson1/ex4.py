def f14(x):
    if x == 0:
        return 6
    elif x == 1:
        return 2
    else:
        return 1 / 78 * f14(x-1) ** 2 - 1 / 52 * f14(x-2) ** 3



#print(foo(15))
#print(foo(3))