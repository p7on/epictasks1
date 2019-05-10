from tkinter import *
import json


TODO = []


def create_file():
    with open('data.json') as data_json:
        TODO = json.load(data_json)
        data_json.close()
    Dicti = {}
    entry_name = task_entry.get()
    Dicti['Task_name'] = entry_name
    entry_category = category_entry.get()
    Dicti['Category'] = entry_category
    entry_time = time_entry.get()
    Dicti['Time'] = entry_time
    TODO.append(Dicti)
    with open('data.json', 'w') as out_file:
        json.dump(TODO, out_file)
        out_file.close()


def load_file():
    with open('data.json') as data_json:
        TODO = json.load(data_json)
        data_json.close()
    for task in TODO:
        print('Task name: ' + task['Task_name'], 'Category: ' + task['Category'], 'Time: ' + task['Time'], sep='\n')


def exit():
    window.destroy()
    print('Bye!')


if __name__ == '__main__':
    window = Tk()
    window.title('Task manager')
    window.resizable(False, False)
    task_variable = StringVar()
    task_label = Label(window, text='Task:').grid(row=0, column=0, padx=30)
    task_entry = Entry(window, textvariable=task_variable, width=20)
    task_entry.grid(row=0, column=1, columnspan=2, sticky=W + E)

    category_variable = StringVar()
    category_label = Label(window, text='Category:').grid(row=1, column=0, padx=15)
    category_entry = Entry(window, textvariable=category_variable)
    category_entry.grid(row=1, column=1, columnspan=2, sticky=W + E)

    time_variable = StringVar()
    time_label = Label(window, text='Time:').grid(row=2, column=0, padx=30)
    time_entry = Entry(window, textvariable=time_variable)
    time_entry.grid(row=2, column=1, columnspan=2, sticky=W + E)

    add_button = Button(window, text='Add task', width=20, command=create_file).grid(row=3, column=0, columnspan=3, sticky=W + E, padx=50)
    show_button = Button(window, text='Show tasks', width=20, command=load_file).grid(row=4, column=0, columnspan=3, sticky=W + E, padx=50)
    exit_button = Button(window, text='Exit', width=20, command=exit).grid(row=5, column=0, columnspan=3, sticky=W + E, padx=50)

    window.mainloop()


'''
#добавить третью колонну (width=, height=)// посмотреть что используется для вывода текста (Text??)
'''
