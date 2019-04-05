def parity(x):
    if x % 2 == 0:
        return 'true'
    else:
        return 'false'


x = int(input('x: '))
print(parity(x))
