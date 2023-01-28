from tkinter import *

pro = Tk()
pro.title('Nikita')
pro.geometry('500x500')

def click():
    pro.geometry('200x200')

def close():
    pro.destroy()

t1 = Label(text='Nickita Uassya', anchor='c', padx=8, pady=8)
t1.pack(fill='both', anchor='c', side='top')
bt = Button(text="Resize", bg='red', compound='top', command=click)
bt.pack(side='top', padx=8, pady=20)
bt2 = Button(text='Close', bg='blue', command=close)
bt2.pack(anchor='c')
pro.mainloop()
