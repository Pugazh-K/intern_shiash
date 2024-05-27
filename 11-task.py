#task - 11: Add buttons like sub, multiply, div and perform operations:

import tkinter.messagebox
from tkinter import *

obj = Tk() #built in class 
obj.geometry('400x400') #form size
obj.title('operations') #form title
obj.configure(bg='aqua') #bg colour

#performing operations
def add():
    num1 = number1.get()
    num2 = number2.get()
    num3 = number3.get()
    data = num1 + num2 + num3
    tkinter.messagebox.showinfo('Result', 'Total: ' + str(data))

def subtract():
    num1 = number1.get()
    num2 = number2.get()
    num3 = number3.get()
    data = num1 - num2 - num3
    tkinter.messagebox.showinfo('Result', 'Difference: ' + str(data))

def multiply():
    num1 = number1.get()
    num2 = number2.get()
    num3 = number3.get()
    data = num1 * num2 * num3
    tkinter.messagebox.showinfo('Result', 'Product: ' + str(data))

def divide():
    num1 = number1.get()
    num2 = number2.get()
    num3 = number3.get()
    try:
        data = num1 / num2 / num3
        tkinter.messagebox.showinfo('Result', 'Quotient: ' + str(data))
    except ZeroDivisionError:
        tkinter.messagebox.showerror('Error', 'Division by zero is not allowed')

#adding labels
Label(obj, text='Enter value A', font=('calibri', 15), bg='aqua').place(x=30, y=30)
Label(obj, text='Enter value B', font=('calibri', 15), bg='aqua').place(x=30, y=80)
Label(obj, text='Enter value C', font=('calibri', 15), bg='aqua').place(x=30, y=130)

#declare variables
number1 = IntVar()
number2 = IntVar()
number3 = IntVar()

#adding textboxes
Entry(obj, textvariable=number1, font=('calibri', 15)).place(x=180, y=30)
Entry(obj, textvariable=number2, font=('calibri', 15)).place(x=180, y=80)
Entry(obj, textvariable=number3, font=('calibri', 15)).place(x=180, y=130)

#adding buttons
Button(obj, text='Add', font=('calibri', 13), bg='blue', fg='white', width=10, height=1, command=add).place(x=50, y=200)
Button(obj, text='Subtract', font=('calibri', 13), bg='blue', fg='white', width=10, height=1, command=subtract).place(x=160, y=200)
Button(obj, text='Multiply', font=('calibri', 13), bg='blue', fg='white', width=10, height=1, command=multiply).place(x=50, y=250)
Button(obj, text='Divide', font=('calibri', 13), bg='blue', fg='white', width=10, height=1, command=divide).place(x=160, y=250)

obj.mainloop() #main func

