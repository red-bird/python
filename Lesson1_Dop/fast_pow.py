def fast_pow(x, y):
    sum = x
    if y == 0:
        return 1
    for _ in range(y):
        sum += fast_mul


print(fast_pow(2, 3))