from tkinter import *
import os
calcgui = Tk()
calcgui.title("计算器")
calcgui.geometry("640x250")
cllbl = Label(calcgui,text="")
cllbl.grid(column=4,row=1)
m1t = Label(calcgui, text="数字")
m1t.grid(column=0, row=0)
t = Label(calcgui, text="运算符号")
t.grid(column=1, row=0)
m2t = Label(calcgui, text="数字")
m2t.grid(column=2, row=0)
ct = Label(calcgui, text="结果")
ct.grid(column=4, row=0)
m1e = Entry(calcgui,width=16)
m1e.grid(column=0,row=1)
t = Entry(calcgui,width=16)
t.grid(column=1,row=1)
m2e = Entry(calcgui,width=16)
m2e.grid(column=2,row=1)
def clicked():
    if t.get()=="+" or t.get()=="-" or t.get()=="*" or t.get()=="/":
        c=eval(str(m1e.get()+t.get()+m2e.get()))
    elif t.get()=="^":
        c=eval(str("pow("+str(m1e.get())+","+str(m2e.get())+")"))
    elif t.get()=="√":
        c=eval(str("pow("+str(m2e.get())+","+str(1/m1e.get()+")")))
    else:
        c=str("")
    cllbl.configure(text=c)
    
def ex():
    calcgui.quit()
def cl():
    m1e.delete(0, END)
    m2e.delete(0, END)
    t.delete(0, END)
    cllbl.configure(text="")
clbtn = Button(calcgui, text="计算", bg="blue", fg="white",command=clicked)
clbtn.grid(column=3,row=1)
exbtn = Button(calcgui, text="退出", bg="red", fg="white",command=ex)
exbtn.grid(column=3,row=2)
clearb = Button(calcgui,text="  C  ",bg="blue",fg="white",command=cl)
clearb.grid(column=3,row=0)
txt1 = Label(calcgui, text="'√' = 'Alt' + '41420'")
txt1.grid(column=1, row=2)
txt2 = Label(calcgui, text="'+' = 'Shift' + '='")
txt2.grid(column=1, row=3)
txt3 = Label(calcgui, text="'^' = 'Shift' + '5'")
txt3.grid(column=1, row=4)
calcgui.mainloop()
