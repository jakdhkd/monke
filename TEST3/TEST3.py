from tkinter import *
lox=Tk()
lox.geometry("400x300")
lox.resizable(0,0)
lox.title("Test")
lox.config(bg="blue")

def chiqish():
    lox.destroy()
def tozalash():
    son1.set("")
    son2.set("")
    natija.set("")
def qoshish():
    a=int(son1.get())
    b=int(son2.get())
    s=a+b
    return natija.set(s)
def ayirish():
    a=int(son1.get())
    b=int(son2.get())
    s=a-b
    return natija.set(s)
def bolish():
    a=int(son1.get())
    b=int(son2.get())
    s=a/b
    return natija.set(s)
def kopaytirish():
    a=int(son1.get())
    b=int(son2.get())
    s=a*b
    return natija.set(s)


son1=StringVar()
son2=StringVar()
natija=StringVar()

son1_entry=Entry(lox,width=25,textvariable=son1,bg="blue").place(x=145,y=65)
son2_entry2=Entry(lox,width=25,textvariable=son2,bg="blue").place(x=145,y=85)
natija_entry3=Entry(lox,width=25,textvariable=natija,bg="blue").place(x=88,y=105)



    


Label(lox,text="Jamshidning Kalkulyatori", font="Algerian 20 bold",bg="blue").pack()
Label(lox,text="Birinchi son:", font="Algerian 15 bold",bg="blue").place(x=0,y=60)
Label(lox,text="Ikkinchi son:", font="Algerian 15 bold",bg="blue").place(x=0,y=80)
Label(lox,text="Natija:", font="Algerian 15 bold",bg="blue").place(x=0,y=100)
Button(lox,text="Qo'shish", font="Algerian 14 bold",bg="green",command=qoshish).place(x=0,y=200)
Button(lox,text="Ayirish", font="Algerian 15 bold",bg="yellow",command=ayirish).place(x=0,y=161)
Button(lox,text="Bo'lish",font="Algerian 15 bold",bg="red",command=bolish).place(x=104,y=161)
Button(lox,text="Ko'paytirish", font="Algerian 15 bold",bg="white",command=kopaytirish).place(x=109,y=200)
Button(lox,text="Chiqish", font="Algerian 15 bold",bg="purple",command=chiqish).place(x=0,y=237)
Button(lox,text="Tozalash",font="Algerian 15 bold",bg="orange",command=tozalash).place(x=102,y=237)

























