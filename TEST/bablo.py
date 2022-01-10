from tkinter import *
from pytube import YouTube

lox=Tk()
lox.geometry("500x300")
lox.resizable(0,0)
lox.title("Mars YouTube Downloader")

Label(lox,text="YouTube Downloader", font="Algerian 20 bold").pack()

link=StringVar()

Label(lox,text="echki", font="Algerian 15 bold").place(x=160,y=60)

link_entry=Entry(lox,width=70,textvariable=link).place(x=32,y=90)

def Downloader():
    url=YouTube(str(link.get()))
    video=url.streams.get_highest_resolution()
    video.download()
    Label(lox,text="SKACHAT QILINDI",font="Algerian 15 bold").place(x=18, y=210)
Button(lox,text="SKACHAT QILMOQ",font="Algerian 15 bold",bg="pale violet red",padx=2,command=Downloader).place(x=180,y=150)
lox.mainloop()


