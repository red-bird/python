from Lesson1_Dop.fast_mul import fast_mul


def fast_pow(x, y):
    sum = x
    flag = False

    if y < 0:
        flag = True

    y = abs(y)

    if y == 0:
        return 1
    for _ in range(y - 1):
        sum = fast_mul(sum, x)
    if flag:
        return 1 / sum
    return sum


print(fast_pow(2, 4))
print(fast_pow(-2, 4))
print(fast_pow(-2, 3))
print(fast_pow(2, -4))