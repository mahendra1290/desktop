'''from tkinter import *

def donothing():
   x = 0
   
root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()'''
import tkinter as tk
from tkinter.colorchooser import *
 
def getColor():
    color = askcolor() 
    print(color[1])
    mw.configure(background=color[1])
    
mw = tk.Tk()
mw.title('COLOR ME!!!')
mw.geometry("500x500") 
mw.configure(background="maroon4")
mw.resizable(0, 0)
tk.Button(text='Select Color', command=getColor).grid(row = 0, column = 1)
 
mw.mainloop()