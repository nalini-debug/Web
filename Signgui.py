from tkinter import *
from datetime import timedelta, date
import datetime
from tkinter import messagebox



def main():
    window=Tk()
    window.title("Know your Astrology")
    l1=Label(window,text="Name")
    l2=Label(window,text="DOB")
    l3=Label(window,text="your Sign is:-")
    l4=Label(window,text="")
    e1=Entry(window,width=10)
    e2=Entry(window,width=10)
    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    l3.grid(row=3,column=1)
    e1.grid(row=1,column=2)
    e2.grid(row=2,column=2)
    l4.grid(row=3,column=2)

    def config():
        a=str(e1.get())
        k=str(e2.get())
        if a.isalpha():
            top = Tk()
            top.geometry("80x60")

            def wel():
                messagebox.showerror("Name Error", "Enter valid name")

            B1 = Button(top, text="Welcome {}".format(a), command=wel)
            B1.place(x=15, y=25)



        else:

            top = Tk()
            top.geometry("80x60")

            def error():
                messagebox.showerror("Name Error", "Enter valid name")

            B1 = Button(top, text="enter valid name", command=error)
            B1.place(x=15, y=25)




        o = k
        j = datetime.datetime.strptime(o, "%B-%d-%Y")
        p = j.date()




        if (p.strftime("%B") == "January"):
          if (p.day <= 22):
            s='capricorn'
          else:
                s='Auarious'

        elif (p.strftime("%B") == "February"):
          if (p.day <= 18):
            s='Aquarious'
          else:
            s='pieces'

        elif (p.strftime("%B") == "March"):
          if (p.day <= 20):
                s='Pieces'
          else:
                s='Aries'

        elif (p.strftime("%B") == "April"):
          if (p.day <= 19):
                s='Aries'
          else:
                s='Taurus'

        elif (p.strftime("%B") == "May"):
          if (p.day <= 20):
                s='Taurus'
          else:
                s='gemini'
        elif (p.strftime("%B") == "June"):
          if (p.day <= 20):
                s='gemini'
          else:
                s='cancer'
        elif (p.strftime("%B") == "Jully"):
          if (p.day <= 22):
                s='cancer'
          else:
                s='leo'
        elif (p.strftime("%B") == "August"):
          if (p.day <= 22):
                print('leo')
          else:
                s='virgo'
        elif (p.strftime("%B") == "September"):
          if (p.day <= 22):
                s='Virgo'
          else:
                s='Libra'
        elif (p.strftime("%B") == "October"):
          if (p.day <= 22):
                s='Libra'
          else:
                s='Scorpio'
        elif (p.strftime("%B") == "November"):
          if (p.day <= 21):
                s='Scorpio'
          else:
                s='Sagittarius'
        elif (p.strftime("%B") == "December"):
          if (p.day <= 21):
                s='Sagittarius'
          else:
              s = 'Capricorn'


        l4.configure(text=str(s))
    b1=Button(window,text="configure",command=config)

    b1.grid(row=4,column=1)

    window.geometry("300x300")
    window.mainloop()
main()
