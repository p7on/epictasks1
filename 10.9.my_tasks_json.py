import json

TODO = []


with open('data.json') as data_json:
    TODO = json.load(data_json)
    data_json.close()
print(TODO)


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
        print(TODO)
    elif key == 3:
        with open('data.json', 'w') as out_file:
            json.dump(TODO, out_file)
            out_file.close()
        print('Saved!')
        break
    else:
        print('This command doesnt exist')
        continue