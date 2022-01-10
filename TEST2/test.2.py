from tkinter import *
lox=Tk()
lox.geometry("700x300")
lox.resizable(0,0)
lox.title("Test")
lox.config(bg="blue")

rasm=PhotoImage(file="book.png")
lox.iconphoto(False,rasm)
contactlist=[
    ["Ali","123456789"],
    ["Vali","987654321"]
    ]


frame=Frame(lox)
frame.pack(side=RIGHT)
scroll=Scrollbar(frame, orient=VERTICAL)
select=Listbox(frame,yscrollcommand=scroll.set,height=6)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)



def chiqish():
    lox.destroy()
def tanlash():
    return int(select.curselection()[0])
def qoshish():
    contactlist.append([ism.get(),tel.get()])
    Select_set()
def taxrirlash():
    contactlist[tanlash()]=[ism.get(),tel.get()]
    Select_set()
def ochirish():
    del contactlist[tanlash()]
    Select_set()
def korish():
    name,number=contactlist[tanlash()]
    ism.set(name)
    tel.set(number)
def tozalash():
    ism.set("")
    tel.set("")

def Select_set():
    contactlist.sort()
    select.delete(0,END)
    for ism,tel in contactlist:
        select.insert(END,ism)
Select_set()





Label(lox,text="Kantaktlar", font="Algerian 20 bold",bg="blue").pack()
Label(lox,text="Ism:", font="Algerian 15 bold",bg="blue").place(x=0,y=60)
Label(lox,text="Raqam:", font="Algerian 15 bold",bg="blue").place(x=0,y=80)
Button(lox,text="Saqlash", font="Algerian 15 bold",bg="green",command=qoshish).place(x=180,y=120)
Button(lox,text="Tozalash", font="Algerian 15 bold",bg="yellow",command=tozalash).place(x=0,y=120)
Button(lox,text="Yangilash",font="Algerian 15 bold",bg="red",command=taxrirlash).place(x=360,y=120)
Button(lox,text="Korish", font="Algerian 15 bold",bg="white",command=korish).place(x=180,y=200)
Button(lox,text="Chiqish", font="Algerian 15 bold",bg="purple",command=chiqish).place(x=0,y=200)
Button(lox,text="O'chirish",font="Algerian 15 bold",bg="orange",command=ochirish).place(x=360,y=200)
ism=StringVar()
tel=StringVar()

ism_entry=Entry(lox,width=50,textvariable=ism,bg="gray").place(x=45,y=65)
tel_entry2=Entry(lox,width=50,textvariable=tel,bg="gray").place(x=85,y=85)








