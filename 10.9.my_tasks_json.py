import json
import os

TODO = []


def doesFileExists(PATH):
    return os.path.exists(PATH)


if doesFileExists('./data.json'):
    print ('Yep, it exists!')
    data_json = open('data.json', 'r')
    with open('data.json') as data_json:
        TODO = json.load(data_json)
        #data_json.close()

else:
    print('It doesnt exist')
    with open('data.json', 'w') as data_json:
        data_json.write('')

        # out_file.close()

TODO = []
'''
data_json = open('data.json', 'w')
with open('data.json') as data_json:
    TODO = json.load(data_json)
    data_json.close()
'''
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
        with open('data.json', 'w') as out_file:
            json.dump(TODO, out_file)
            out_file.close()
        print('Saved!')
        break
    else:
        print('This command doesnt exist')
        continue

#TODO = []
