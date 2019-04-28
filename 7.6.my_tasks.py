TODO = []
task_name = ['Task name:', 'Category:', 'Time:']

while True:
    welcome_text = 'Simple TODO:\n 1 to Add task\n 2 to show task list\n 3 for exit'
    print(welcome_text)
    key = int(input('Insert the number: '))
    if key == 1:
        TODO.append([[print(name), input()][1] for name in task_name])
        print(TODO)
    elif key == 2:
        for task in TODO:
            print('Task name: ' + task[0], 'Category: ' + task[1], 'Time: ' + task[2], sep='\n')
    elif key == 3:
        break
    else:
        print('This command doesnt exist')
        continue
