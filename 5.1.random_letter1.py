import random
a = ['самовар', 'весна', 'лето']
word = random.choice(a)  # рандомное слово
letter = random.choice(word)  # рандомная буква
letter_index = word.index(letter)  # находим индекс рандомной буквы
word1 = list(word)  # преобразуем выбранное слово в список
word1[letter_index] = '?'  # заменяем рандомную букву на ?
newword = "".join(word1)
print(newword)

guess = input('Введите букву: ')
if guess == letter:
    print('Победа!')
else:
    print('Увы! Попробуйте в другой раз', '\nСлово:', word)
