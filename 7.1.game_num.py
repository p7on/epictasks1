from random import randint
a = randint(0, 10)  # от 0 до 10
k = int(input('Enter the number of attempts: '))
n = ""

# for x in range(k):
while True:
    for x in range(k):
        n = input('Enter the number or code word: ')
        if n == str(a) or n == 'Exit':
            print('Loop is over')
            break
        elif n > str(a):
            print('n > a')
        else:
            print('n < a')
    break
