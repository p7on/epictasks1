s = input('string: ')
n = int(input('n: '))


def str_n(s, n):
    if n <= len(s):
        return s.upper()
    else:
        return s


print(str_n(s, n))

'''
не работает если переменная объявлена после функции (??)
'''
