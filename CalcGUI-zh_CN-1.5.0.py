from tkinter import *
import data.pyglet.font
calcgui = Tk()
calcgui.title("计算器")
calcgui.geometry("640x250")
cllbl = Label(calcgui,text="",font="HarmonyOS Sans SC")
cllbl.place(x=350, y=32)
m1t = Label(calcgui, text="数字",font="HarmonyOS Sans SC")
m1t.place(x=25, y=8)
t = Label(calcgui, text="运算符号",font="HarmonyOS Sans SC")
t.place(x=125, y=8)
m2t = Label(calcgui, text="数字",font="HarmonyOS Sans SC")
m2t.place(x=200, y=8)
ct = Label(calcgui, text="结果",font="HarmonyOS Sans SC")
ct.place(x=345, y=10)
m1e = Entry(calcgui,width=16)
m1e.place(x=0, y=32)
t = Entry(calcgui,width=8)
t.place(x=118, y=32)
m2e = Entry(calcgui,width=16)
m2e.place(x=180, y=32)
pyglet.font.add_file("data/res/fonts/hmsansr.ttf")
pyglet.font.load("data/res/fonts/hmsansr.ttf")
def clicked():
    if m1e.get()=="":
        a1()
    else:
        if t.get()=="+" or t.get()=="-" or t.get()=="*" or t.get()=="/":
            c=eval(str(m1e.get()+t.get()+m2e.get()))
        elif t.get()=="^":
            c=pow(float(m1e.get),float(m2e.get))
        elif t.get()=="**":
            c=pow(float(m1e.get()),float(m2e.get()))
        elif t.get()=="√":
            c=float(pow(float(m2e.get()),1/float(m1e.get())))
        else:
            c=str("")

        cllbl.configure(text=c)
def a1():
    if cllbl.cget("text")!="":
        m1e.delete(0, END)
        m1e.insert(0,cllbl.cget("text"))
        calcgui.after(0,clicked)
    elif t.get()!="√":
        m1e.insert(0,"0")
        calcgui.after(0,clicked)
    else:
        m1e.insert(0,"2")
        calcgui.after(0,clicked)
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
clbtn = Button(calcgui, text="计算", bg="blue", fg="white",font="HarmonyOS Sans SC",command=clicked)
clbtn.place(x=300, y=30)
exbtn = Button(calcgui, text="退出", bg="red",font="HarmonyOS Sans SC", fg="white",command=ex)
exbtn.place(x=300, y=60)
clearb = Button(calcgui,text="  C  ",bg="blue",font="HarmonyOS Sans SC",fg="white",command=cl)
clearb.place(x=300, y=0)
copyb = Button(calcgui, text="复制", bg="blue",font="HarmonyOS Sans SC", fg="white",command=copy)
copyb.place(x=335,y=60)
calcgui.mainloop()
