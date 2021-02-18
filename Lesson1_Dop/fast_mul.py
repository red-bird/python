def fast_mul(x, y):
    tab1 = []
    tab2 = []
    tab1.append(x)
    tab2.append(y)

    flag = False
    # 1st column
    if x < 0:
        flag = True

    x = abs(x)
    while x > 1:
        x //= 2
        tab1.append(x)

    # 2nd column + calculate
    sum = 0
    for e in tab1:
        tab2.append(y * 2)
        y *= 2
        if e % 2 == 1:
            sum += tab2[tab1.index(e)]
    if flag:
        return sum * -1
    return sum


# print(fast_mul(10, 15))
# print(fast_mul(15, 15))
# print(fast_mul(5, 12))
# print(fast_mul(-15, -15))
# print(fast_mul(2, 3))

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