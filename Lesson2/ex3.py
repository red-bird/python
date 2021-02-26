def distinctCols(matrix):
    res = matrix
    res = transpose(res)
    distinctRows(res)
    res = transpose(res)
    return res


def distinctRows(matrix):
    for i in range(len(matrix)-1):
        if matrix[i] == matrix[i+1]:
            del matrix[i+1]


def transpose(matrix):
    res = [[None for i in range( (len(matrix)) )] for i in range( (len(matrix[0])) )]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res[j][i] = matrix[i][j]
    return res


def convert(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                matrix[i][j] = 'да'
            elif matrix[i][j] == '0':
                matrix[i][j] = 'нет'
            elif matrix[i][j][0] == '+':
                matrix[i][j] = matrix[i][j][:2] + ' ' + matrix[i][j][3:]
                matrix[i][j] = matrix[i][j][:6] + ' ' + matrix[i][j][7:]
                matrix[i][j] = matrix[i][j][:13] + '' + matrix[i][j][14:]
            else:
                matrix[i][j] = str(matrix[i][j]).replace("‐", ".")
                # matrix[i][j] = matrix[i][j][:2] + '.' + matrix[i][j][3:]
                # matrix[i][j] = matrix[i][j][:5] + '.' + matrix[i][j][6:]


def f23(matrix):
    distinctRows(matrix)
    matrix = distinctCols(matrix)
    matrix = transpose(matrix)
    convert(matrix)
    # print(*matrix, sep='\n')


# f23(
#     [
#         ['0', '+7(557)381‐21‐67', '26‐09‐99', '26‐09‐99'],
#         ['1', '+7(570)330‐47‐91', '08‐12‐99', '08‐12‐99'],
#         ['1', '+7(599)301‐83‐74', '22‐01‐02', '22‐01‐02'],
#         ['1', '+7(599)301‐83‐74', '22‐01‐02', '22‐01‐02']
#     ]
# )