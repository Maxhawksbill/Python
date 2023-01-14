from tkinter import *

pro = Tk()
pro.geometry('200x200')

def click():
    print('clicked')
    pro.geometry('100x100')

def close():
    pro.destroy()

bt = Button(text="Button", bg='red', command=click)
bt.pack()
bt2 = Button(text='Close', bg = 'blue', command = close)
bt2.pack(anchor = 'w')
pro.mainloop()
