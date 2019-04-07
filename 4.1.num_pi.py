from math import *
x = int(input('x: '))


def num_py(x):
    return('{p:.{x}f}'.format(p=pi, x=x))


print('pi: ', num_py(x))

'''
не работает если переменная объявлена после функции (??)
'''
