import json

TODO = []

while True:
    welcome_text = 'Simple TODO:\n 1 to Add task\n 2 to show task list\n 3 for exit'
    print(welcome_text)
    key = int(input('Insert the number: '))
    if key == 1:
        Dicti = {}
        Dicti['Task_name'] = input('Task name: ')
        Dicti['Category'] = input('Category: ')
        Dicti['Time'] = input('Time: ')
        TODO.append(Dicti)
    elif key == 2:
        for task in TODO:
            print('Task name: ' + task['Task_name'], 'Category: ' + task['Category'], 'Time: ' + task['Time'], sep='\n')
    elif key == 3:
        with open('data.json', 'a') as out_file:
            json.dump(TODO, out_file)
        print('Saved!')
        break
    else:
        print('This command doesnt exist')
        continue
