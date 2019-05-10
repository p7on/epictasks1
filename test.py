from tkinter import *


def click():
    while True:
        entered_text = text_entry.get()
        if entered_text .isdigit() == False:
            error = Label(window, text="Try again", bg="black", fg="red", font="none 11").grid(row=3, column=2, sticky=W).pack()
        else:
            break
    return True


window = Tk()

window.title("Tax calculator")
window.configure(background="black")


monto = Label(window, text="¿What is your debt?", bg="black", fg="white", font="none 12 bold")
monto.grid(row=1, column=0, sticky=W)

text_entry = Entry(window, width=20, bg="white")
text_entry.grid(row=2, column=2, sticky=W)

output = Button(window, text="Enter", width=6, command=click)
output.grid(row=3, column=0, sticky=W)
