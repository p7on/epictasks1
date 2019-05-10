from tkinter import *
import json

TODO = []


def create_file():
    '''
    Fuction open data.json file, load content from it to TODO list, create dictionaries and add it to TODO list, after adding closes the file
    '''
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
    '''
     Function opens data.json file, load content from it to TODO list and print all the content to Tkinter's GUI in TEXT widget
    '''
    with open('data.json') as data_json:
        TODO = json.load(data_json)
        data_json.close()
    for task in TODO:
        result_text.insert(1.0, '' +
                           'Task name: ' + task['Task_name'] +
                           '\n' 'Category: ' + task['Category'] +
                           '\n' 'Time: ' + task['Time'] +
                           '\n')
    data_json.close()


def exit():
    '''Simple function, just closes the GUI'''
    window.destroy()
    print('Bye!')


if __name__ == '__main__':
    window = Tk()
    window.geometry('640x160')  # Set the size of the window
    window.title('Task manager')  # Change title of task manager
    window.resizable(False, False)  # Make window unresizeble

    frame = Frame(window, background="bisque")  # Create the frame for scrollbar

    scroll = Scrollbar(frame)  # Create the scrollbar
    scroll.grid(row=3, column=4)  # ???

    task_variable = StringVar()  # Variable for task_entry
    task_label = Label(window, text='Task:').grid(row=0, column=0, padx=30)  # Legend next to entry
    task_entry = Entry(window, textvariable=task_variable, width=20)
    task_entry.grid(row=0, column=1, columnspan=2, sticky=W + E)

    category_variable = StringVar()  # Variable for category_entry
    category_label = Label(window, text='Category:').grid(row=1, column=0, padx=15)  # Legend next to entry
    category_entry = Entry(window, textvariable=category_variable)
    category_entry.grid(row=1, column=1, columnspan=2, sticky=W + E)

    time_variable = StringVar()  # Variable for time_entry
    time_label = Label(window, text='Time:').grid(row=2, column=0, padx=30)  # Legend next to entry
    time_entry = Entry(window, textvariable=time_variable)
    time_entry.grid(row=2, column=1, columnspan=2, sticky=W + E)

    add_button = Button(window, text='Add task', width=20, command=create_file).grid(row=3, column=1, columnspan=2, sticky=W + E, padx=50)  # Add task button
    show_button = Button(window, text='Show tasks', width=20, command=load_file).grid(row=4, column=1, columnspan=2, sticky=W + E, padx=50)  # Show tasks button
    exit_button = Button(window, text='Exit', width=20, command=exit).grid(row=5, column=1, columnspan=2, sticky=W + E, padx=50)  # Exit button

    result_text = Text(frame, yscrollcommand=scroll.set, width=30, height=10)
    result_text.grid(row=0, rowspan=6, column=3)

    scroll.config(command=result_text.yview)

    frame.grid(row=0, rowspan=6, column=3)

    window.mainloop()

