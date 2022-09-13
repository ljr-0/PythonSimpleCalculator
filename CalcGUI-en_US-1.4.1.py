from tkinter import *
import os
calcgui = Tk()
calcgui.title("Calculator")
calcgui.geometry("640x250")
cllbl = Label(calcgui,text="")
cllbl.place(x=400, y=32)
m1t = Label(calcgui, text="Number")
m1t.place(x=25, y=8)
t = Label(calcgui, text="symbol")
t.place(x=125, y=8)
m2t = Label(calcgui, text="Number")
m2t.place(x=200, y=8)
ct = Label(calcgui, text="Result")
ct.place(x=400, y=10)
m1e = Entry(calcgui,width=16)
m1e.place(x=0, y=32)
t = Entry(calcgui,width=8)
t.place(x=118, y=32)
m2e = Entry(calcgui,width=16)
m2e.place(x=180, y=32)
def clicked():
    if t.get()=="+" or t.get()=="-" or t.get()=="*" or t.get()=="/":
        c=eval(str(m1e.get()+t.get()+m2e.get()))
    elif t.get()=="^" or "**":
        c=eval(str("pow("+str(m1e.get())+","+str(m2e.get())+")"))
    elif t.get()=="√":
        c=eval(str("pow("+str(m2e.get())+","+str(1/m1e.get()+")")))
    else:
        c=str("")
    if m1e.get()=="":
        a1()
    cllbl.configure(text=c)
def a1():
    if cllbl.cget("text")!="":
        m1e.delete(0, END)
        m1e.insert(0,cllbl.cget("text"))
        calcgui.after(0,clicked)
    else:
        m1e.insert(0,"0")
def ex():
    calcgui.destroy()
def cl():
    m1e.delete(0, END)
    m2e.delete(0, END)
    t.delete(0, END)
    cllbl.configure(text="")
def copy():
    calcgui.clipboard_clear()
    calcgui.clipboard_append(cllbl.cget("text"))
clbtn = Button(calcgui, text="Calculation", bg="blue", fg="white",command=clicked)
clbtn.place(x=300, y=30)
exbtn = Button(calcgui, text="Exit", bg="red", fg="white",command=ex)
exbtn.place(x=300, y=60)
clearb = Button(calcgui,text="  C  ",bg="blue",fg="white",command=cl)
clearb.place(x=300, y=0)
copyb = Button(calcgui, text="Copy", bg="blue", fg="white",command=copy)
copyb.place(x=335,y=60)
txt1 = Label(calcgui, text="'√' = 'Alt' + '41420'")
txt1.place(x=95, y=60)
txt2 = Label(calcgui, text="'+' = 'Shift' + '='")
txt2.place(x=95, y=85)
txt3 = Label(calcgui, text="'^' = 'Shift' + '5'")
txt3.place(x=95, y=110)
calcgui.mainloop()
