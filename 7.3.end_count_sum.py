result = 0
while True:
    try:
        n = input('Enter the number or stop to exit: ').lower()
        if n == 'stop':
            break
        else:
            result += float(n)
    except ValueError:
        print('Error')
print(result)

# Как сделать так чтобы выход по ключу был вне зависимости от его регистра (верхний/нижний)? Помимо доп. условия в if
