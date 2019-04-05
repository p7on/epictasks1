'''
not ready
'''
film = input('Select movie: ')
date = input('Today or tommorow?: ')
time = int(input('Choose time: '))
tickets = int(input('Quanity of tickets: '))
price = int(input('Select price: ')) * tickets

print('\nFilm: ', film, '\nDay: ', date, '\nTime: ', time, '\nQuanity of tickets: ', tickets)

if film == 'Пятница' or film == 'Чемпионы' or film == 'Пернатая банда':
    if date == 'Tommorow':
        price *= 0.95
    elif tickets >= 20:
        price *= 0.8
    print(price)
else:
    print('Error')
