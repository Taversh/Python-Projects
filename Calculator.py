# |>>> Taversh <<<| #

                                        # This is a Program to make a Calculator #

import tkinter
from tkinter import *

root = Tk()
root.title("Calculator by @ |>>> Taversh <<<|")
root.geometry("570x600+100+300")
root.resizable(False,False)
root.config(background="dark grey")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result ="ERROR"
            equation =""    
    label_result.config(text=result)       



label_result = Label(root, anchor= W, width=25, height=2, text="", font=("orbital",30,"bold"))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("orbital",30,"bold"), bd=1, fg="white", bg="red", relief= "raised", command=lambda: clear()).place(x=10,y=115)
Button(root, text="/", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("/")).place(x=150,y=115)
Button(root, text="%", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("%")).place(x=290,y=115)
Button(root, text="*", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("*")).place(x=430,y=115)

Button(root, text="7", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("7")).place(x=10,y=210)
Button(root, text="8", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("8")).place(x=150,y=210)
Button(root, text="9", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("9")).place(x=290,y=210)
Button(root, text="-", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("-")).place(x=430,y=200)

Button(root, text="4", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("4")).place(x=10,y=310)
Button(root, text="5", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("5")).place(x=150,y=310)
Button(root, text="6", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("6")).place(x=290,y=310)
Button(root, text="+", width=5, height=4, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("+")).place(x=431,y=290)

Button(root, text="1", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("1")).place(x=10,y=410)
Button(root, text="2", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("2")).place(x=150,y=410)
Button(root, text="3", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("3")).place(x=290,y=410)

Button(root, text="=", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="navy blue", relief= "raised", command=lambda: calculate()).place(x=431,y=510)
Button(root, text="0", width=11, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show("0")).place(x=10,y=510)
Button(root, text=".", width=5, height=1, font=("arial",30,"bold"), bd=1, fg="white", bg="grey", relief= "raised", command=lambda: show(".")).place(x=290,y=510)





root.mainloop()

#//////////////    //////////////
#     ///               ///
#    ///               ///
#   ///          \\\  ///
#  ///       O    \\\///