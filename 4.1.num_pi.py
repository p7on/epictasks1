from math import *


def num_py(x):
    return '{p:.{x}f}'.format(p=pi, x=x)


x = int(input('x: '))
print('pi: ', num_py(x))

'''
@Необязательно переназначать переменные в .format.
если пишу: '{pi:.{x}f}'.format(pi, x), то выдает ошибку:
Traceback (most recent call last):
  File "4.1.num_pi.py", line 9, in <module>
    print('pi: ', num_py(x))
  File "4.1.num_pi.py", line 5, in num_py
    return '{pi:.{x}f}'.format(pi, x)
KeyError: 'pi'

если '{p:.{x}f}'.format(p=pi, x), то

  File "4.1.num_pi.py", line 5
    return '{p:.{x}f}'.format(p=pi, x)
                                   ^
SyntaxError: positional argument follows keyword argument
'''
