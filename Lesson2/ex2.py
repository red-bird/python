def f22(x):
    mask = 0xffffffff
    a = (mask & 0x0000007f)
    a = (a & x)  << 16
    b = (mask & 0x00000f80)
    b = (b & x) >> 7 << 23
    c = (mask & 0x01FFF000)
    c = (c & x) >> 12
    d = (mask & 0x1E000000)
    d = (d & x) >> 25 << 28
    e = (mask & 0xE0000000)
    e = (e & x) >> 29 << 13
    res = a | b | c | d | e
    return res


# print(f22(0x390fff97))
# print(f22(0xd47c81d1))