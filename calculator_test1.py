# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:38:22 2020

@author: HP
"""

from tkinter import * 
top = Tk()  
top.geometry("400x250")
def num_error():
    label_text.set("N.B.:")
    text.set("Please enter a valid Number")
def num_sum():
    try:
        res = int(e1.get())+int(e2.get())
        label_text.set("Addition (+): ")
        text.set(res)
    except:
        num_error()
def num_sub():
    try:
        res = int(e1.get())-int(e2.get())
        label_text.set("Substraction (-): ")
        text.set(res)
    except:
        num_error()
def num_mul():
    try:
        res = int(e1.get())*int(e2.get())
        label_text.set("Multiplication (X): ")
        text.set(res)
    except:
        num_error()
def num_div():
    try:
        res = int(e1.get())/int(e2.get())
        label_text.set("Division (/): ")
        text.set(res)
    except(ArithmeticError):
        label_text.set("N.B.:")
        text.set("You can't divide by zero")
    except (ValueError):
        num_error()    
text=StringVar();
label_text=StringVar();
top.title("Calculator")  
a= Label(top, text = "First Number",padx=20,font="timesnewroman").grid(row=0, column=0)  
b = Label(top, text = "Second number",padx=20,font="timesnewroman").grid(row=1, column=0)

r = Label(top, text = "",textvariable=label_text).grid(row=4, column=0)   
result=Label(top, text="", textvariable=text).grid(row=4, column=1, sticky=W)

e1 = Entry(top)
e1.grid(row=0, column=1)   
e2 = Entry(top)
e2.grid(row=1, column=1) 

addbtn = Button(top, text = "+",command=num_sum,padx=10)
#addbtn.grid(row=5, column=0)
addbtn.place(x = 50, y = 80) 

subbtn = Button(top, text = "-",command=num_sub,padx=10)
#subbtn.grid(row=5, column=1) 
subbtn.place(x = 100, y = 80) 
 
mulbtn = Button(top, text = "X",command=num_mul,padx=10)
#mulbtn.grid(row=5, column=2) 
mulbtn.place(x = 150, y = 80) 

divbtn = Button(top, text = "/",command=num_div,padx=10)
#divbtn.grid(row=5, column=3)  
divbtn.place(x = 200, y = 80)   

top.mainloop()  