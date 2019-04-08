s = input('string: ')


def str_n(s, n):
    if n < len(s):
        return s.upper()
    else:
        return s


n = int(input('n: '))
print(str_n(s, n))
