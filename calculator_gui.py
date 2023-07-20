from tkinter import *

window=Tk()


def button_press(num):
    global equation_text
    equation_text=equation_text+str(num)

    equation_label.set(equation_text)




def equal():
    global equation_text
    try:
        total=str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text=""
    except ZeroDivisionError:
        equation_label.set("arithematic error")
        equation_text=''


def clear():
    global equation_text

    equation_label.set("")
    equation_text=""




window.title("Calculator")
window.geometry("500x500")
window.configure(bg='#669999')


equation_text=""
equation_label=StringVar()

label=Label(window,textvariable=equation_label,width=40,height=3,bg="white",fg="black")
label.pack()

frame=Frame(window)
frame.pack()





b1=Button(frame,text=1,width=9,height=4,command=lambda:button_press(1),bg='black',fg="white")
b2=Button(frame,text=2,width=9,height=4,command=lambda:button_press(2),bg='black',fg="white")
b3=Button(frame,text=3,width=9,height=4,command=lambda:button_press(3),bg='black',fg="white")
b4=Button(frame,text=4,width=9,height=4,command=lambda:button_press(4),bg='black',fg="white")
b5=Button(frame,text=5,width=9,height=4,command=lambda:button_press(5),bg='black',fg="white")
b6=Button(frame,text=6,width=9,height=4,command=lambda:button_press(6),bg='black',fg="white")
b7=Button(frame,text=7,width=9,height=4,command=lambda:button_press(7),bg='black',fg="white")
b8=Button(frame,text=8,width=9,height=4,command=lambda:button_press(8),bg='black',fg="white")
b9=Button(frame,text=9,width=9,height=4,command=lambda:button_press(9),bg='black',fg="white")
b0=Button(frame,text=0,width=9,height=4,command=lambda:button_press(0),bg='black',fg="white")

plus=Button(frame,text='+',width=9,height=4,command=lambda:button_press('+'),bg='black',fg="white")
minus=Button(frame,text='-',width=9,height=4,command=lambda:button_press('-'),bg='black',fg="white")
multiply=Button(frame,text='*',width=9,height=4,command=lambda:button_press('*'),bg='black',fg="white")
divide=Button(frame,text='/',width=9,height=4,command=lambda:button_press('/'),bg='black',fg="white")
equal=Button(frame,text='=',width=9,height=4,command=equal,bg='orange',fg="black")
decimal=Button(frame,text='.',width=9,height=4,command=lambda:button_press('.'),bg='black',fg="white")
clear=Button(window,text='clear',width=40,height=4,command=clear,bg='orange',fg="black")

clear.pack()

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

plus.grid(row=0,column=3)


b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

minus.grid(row=1,column=3)


b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)

multiply.grid(row=2,column=3)


b0.grid(row=3,column=0)

decimal.grid(row=3,column=1)
equal.grid(row=3,column=2)

divide.grid(row=3,column=3)




window.mainloop()