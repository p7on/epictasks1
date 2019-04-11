result = 0
while True:
    try:
        n = input('Enter the number or stop to exit: ')
        if n == 'stop':
            break
        elif int(n) > 0:
            result += int(n)
    except ValueError:
        print('Error')
print(result)

# Как сделать так чтобы выход по ключу был вне зависимости от его регистра (верхний/нижний)? Помимо доп. условия в if
