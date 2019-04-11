result = 0
while True:
    n = input('Enter the number or stop to exit: ')
    if n == 'stop':
        break
    else:
        result += int(n)
print(result)

#Как сделать так чтобы выход по ключу был вне зависимости от его регистра (верхний/нижний)? Помимо доп. условия в if
