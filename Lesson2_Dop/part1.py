import random
import sys

#
# s = ['000', '0', '132', '561', 'asd', '4a4', '653', '53461']
# res = []
# # 1
# print([int(x) for x in s if x.isdigit()])
#
# # 2
# print(len(set(s)))
#
# # 3
# print(s[::-1])
#
# # 4
# var = '0'
# print([i for i, x in enumerate(s) if x == var])
#
# # 5
# print("5---------")
# print(''.join((s[::2])))
#
# # 6
# print(max(s, key=len))
#
# # 24 chars
# i = 1
# print('mcwuoocdwhe'[i::3])  # 19 символов
#
#
# # generate groups
#
# def generate_groups():
#     res = []
#     for i in range(1, 26):
#         res.append('K' + str(i))
#     for i in range(1, 14):
#         res.append('B' + str(i))
#     for i in range(1, 3):
#         res.append('M' + str(i))
#     for i in range(1, 11):
#         res.append('H' + str(i))
#
#     return res
#
#
# print(generate_groups())
#
# # zip / transpose (* - unpacking)
# tmp = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
# print([*zip(*tmp)])
#
#
# # referat
#
# def gen_referat():
#     part1 = (
#     'Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,', 'Вместе с тем,',
#     'С другой стороны,')
#     part2 = ('парадигма цифровой экономики', 'контeкст цифровой трансформации', 'диджитализация бизнeс-процессов',
#              'прагматичный подход к цифровым платформам', 'совокупность сквозных тeхнологий',
#              'программа прорывных исслeдований', 'ускорeниe блокчeйн-транзакций', 'экспоненциальный рост Big Data')
#     part3 = ["открывает новые возможности для", "выдвигает новые требования", "несёт в себе риски",
#              "расширяет горизонты", "заставляет искать варианты",
#              "не оставляет шанса для", "повышает вероятность", "обостряет проблему"]
#     part4 = ["дальнейшего углубления", "бюджетного финансирования", "синергетического эффекта",
#              "компрометации конфиденциальных", "универсальной коммодитизации",
#              "несанкционированной кастомизации", "нормативного регулирования", "практического применения"]
#     part5 = ["знаний и компетенций.", "непроверенных гипотез.", "волатильных активов.",
#              "опасных экспериментов.", "государственно-частных партнёрств.",
#              "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
#     return random.choice(part1) + " " + random.choice(part2) + " " + random.choice(part3) + " " + random.choice(
#         part4) + " " + random.choice(part5)
#
#
# print(gen_referat())
#
#
# # print
#
# def printHM(*args, sep=' ', end='\n', file=sys.stdout):
#     file.write(sep.join(str(i) for i in args) + end)
#
#
# print('banana', '1234', -2, [27, 51, ('frog', 12345), {247: 14}, True, None], sep='\t', end='the end\n')
# printHM('banana', '1234', -2, [27, 51, ('frog', 12345), {247: 14}, True, None], sep='\t', end='the end\n')
#
#
# # gen array
#
# def gen_array(*dim):
#     return [*dim]
#
#
# arr = gen_array([1, 2], [3, 4], [5, 6])
# print(arr[1][0])
# print(arr)
#
# # FIO

# names = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Илья', 'Кирилл', 'Михаил', 'Никита',
#          'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван', 'Денис', 'Евгений', 'Тимофей', 'Владислав', 'Игорь',
#          'Владимир', 'Павел', 'Руслан', 'Марк', 'Константин', 'Тимур', 'Олег', 'Ярослав', 'Антон', 'Николай']
# ignore = ['Ю', 'Ь', 'Ъ', 'Й', 'Ё', 'Ы']
# alphabet = [chr(x) for x in range(ord('А'), ord('Я') + 1) if chr(x) not in ignore]
# end_of_lastname = ['ов', 'ев', 'ин', 'ын', 'ский', 'цкий', 'ской', 'цкой', 'ой', 'ий', 'енков', 'их', 'ых', 'ко']
# consonant_letters = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
# vowel_letters = ['а', 'я', 'о', 'е', 'у', 'ю', 'ы', 'и', 'э', 'е']
#
#
# def gen_fio():
#     s = random.choice(names) + " " + random.choice(alphabet) + ". "
#     for i in range(random.randint(1, 3)):
#         if i == 0:
#             s += random.choice(consonant_letters).upper()
#         else:
#             s += random.choice(consonant_letters)
#         s += random.choice(vowel_letters)
#     s = s + random.choice(consonant_letters) + random.choice(end_of_lastname)
#     return s
#
#
# print(gen_fio())
# print(gen_fio())


def bar(text):
    a = []
    for i in range(0, len(text)):
        a.append("")
        for j in range(i, len(text)):
            a[i] += text[j]
        for j in range(0, i):
            a[i] += text[j]
    a.sort()
    res = ""
    for i in range(0, len(text)):
        res += a[i][len(text) - 1]
        if a[i] == text:
            pos_rev = i

    return (res, pos_rev)


def reverse_bar(text, pos):
    a = []
    for i in range(0, len(text)):
        a.append([])
        for j in range(0, len(text)):
            a[i].append('')
    for i in range(len(text) - 1, -1, -1):
        for j in range(0, len(text)):
            a[j][i] = text[j]
        a.sort()
    res = ""
    for i in range(0, len(text)):
        res += a[pos][i]
    return res


res_tuple = bar("ABACABA")
print(res_tuple[0])
print(reverse_bar(res_tuple[0], res_tuple[1]))
