import tkinter as tk
from tkinter import *
import re


def o():

     window=Tk()
     window.title('Email validation')
     canvas = Canvas(window, width=300, height=300)
     a = PhotoImage(file='C:\\Users\\asd\\Downloads\\nat.png')
     canvas.create_image(0, 10, anchor=NW, image=a)
     canvas.create_text(130, 20, fill="darkblue", font="Times 20 italic bold", text='  check validity of Email ')
     canvas.create_text(100, 50, fill="darkblue", font=20, text='Emailid:-')
     e = tk.Entry(window)
     canvas.create_window(100, 70, window=e)
     canvas.update()
     def check():
            e2 = e.get()
            s="^\w{0,15}@gmail.com"
            if re.search(s, e2):
             canvas.create_text(150, 200, fill="darkblue", font='Times 20 italic bold', text='valid Id')
            else:
             canvas.create_text(150, 200, fill="darkblue", font="Times 20 italic bold", text='Invalid Email')

     b= tk.Button(text='validate', command=check, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
     canvas.create_window(150, 90, window=b)

     window.geometry("300x300")
     canvas.pack()
     window.mainloop()
o()
