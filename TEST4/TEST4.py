from tkinter import *
from PIL import Image,ImageTk
from gtts import gTTS
from playsound import playsound
lox=Tk()
lox.geometry("500x300")
lox.resizable(0,0)
lox.title("Test")
lox.config(bg="blue")
def Baqirish():
    Habar=boq.get()
    speech=gTTS(text=Habar)
    speech.save("TEST1.mp3")
    playsound("TEST1.mp3")


rasm1=PhotoImage(file="lox.png")
lox.iconphoto(False,rasm1)
rasm2=ImageTk.PhotoImage(Image.open("JoJo.jpg"))
Fon=Label(image=rasm2)
Fon.pack()



boq=StringVar()
Entry(lox,width=50,textvariable=boq,bg="orange").place(x=145,y=65)
Label(lox,text="Karoc cho'tki narsa", font="Algerian 20 bold",bg="orange").pack()
Label(lox,text="Matni echki:", font="Algerian 15 bold",bg="orange").place(x=0,y=60)
Button(lox,text="Baqirish", font="Algerian 14 bold",bg="green",command=Baqirish).place(x=0,y=200)
Button(lox,text="Chiqish", font="Algerian 14 bold",bg="red",).place(x=400,y=200)
Label(lox,text="O'g'irlagan o'sha", font="Algerian 15 bold",bg="orange").place(x=0,y=250)


lox.mainloop()
