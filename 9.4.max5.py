def max_sequence(seq):
    test = []
    for counter in seq(counter, counter + 4):
        test.append(counter)
    return test


print(max_sequence(max_sequence))


max_sequence([1, 3, 1, 1, 4, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 3, 2, 4, 4, 4])
#new_list = [x for x in max_sequence ]
#max_sequence([1, 5, 7, 2, 9, 2, 9, 2, 5, 3, 7, 6, 3, 3, 7, 4, 4, 1, 9, 5])
if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Разбиваем список на списки по 5
# Складываем значения, передаем одной переменной
# Разбиваем следующий список, суммируем, передаем другой переменной
# Сравниваем значения этих переменных, большую из них оставляем
