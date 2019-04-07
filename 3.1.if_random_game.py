import random
a = random.randint(0, 4)
b = int(input('b: '))
if a == b:
    print('You win')
elif a > b:
    print('a > b')
else:
    print('a < b')

'''
можно прикольнее сделать через цикл:
while b != a:
    b = int(input())
    ...
'''
