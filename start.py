#----------------------------------------------MAIN PAGE CODE-----------------------------------------


from tkinter import *
from tkinter import simpledialog
import time
#---files-----
import trash
import browser
import aging
import function1
import fol
import restart
import flip
import amo 
import calculator
import snake
import screenshot
import chrome
import user
import vi
import vlc
import shotwell
import filemanager
import ubuntusoftware
import editor
import cheese
import setting
#import maze_u
#---------------

root = Tk()
root.title("My Desktop")
root.geometry("5000x5000")


#-----------------------------------------------------------------------

answer = simpledialog.askstring("Input", "What is your first name?",  parent=root)
if answer is not None:
    print("Your first name is ", answer)
else:
    print("You don't have a first name?")

#----------------------------------------------------------------------------------------
#scrollbar = Scrollbar(root)
#scrollbar.grid( column = 29)



def logout():
    answer = "None"
mb =  Menubutton ( root, text = answer) 
mb.grid() 
mb.menu  =  Menu ( mb, tearoff = 0 ) 
mb["menu"]  =  mb.menu 
cVar  = IntVar() 
aVar = IntVar() 
mb.menu.add_checkbutton ( label =answer ) 
mb.menu.add_checkbutton ( label = 'setting', command = setting.main ) 
mb.menu.add_checkbutton ( label = 'logout', command = root.quit) 
mb.grid(row = 0, column = 13) 

#----------------------------------------------TIME--------------------------------------------------

time1 = ''
clock = Label(root,anchor = N, font=('times', 20, 'bold'), bg="pink", height = 1,width = 10)
#clock.pack(fill=BOTH)
clock.grid(row = 0, column = 12) 

def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(200, tick)

tick()

#----------------------------------------------------------------------------------------
photo1 = PhotoImage(file = "/home/naina/naina_python/abcd.png")
photoimage1 = photo1.subsample(4, 4)

photo2 = PhotoImage(file = "/home/naina/naina_python/download.png")
photoimage2 = photo2.subsample(5, 5)

photo3 = PhotoImage(file = "/home/naina/naina_python/ter.png")
photoimage3 = photo3.subsample(12, 12)

photo4 = PhotoImage(file = "/home/naina/naina_python/shut.png")
photoimage4 = photo4.subsample(5, 5)

photo5 = PhotoImage(file = "/home/naina/naina_python/restart1.png")
photoimage5 = photo5.subsample(4, 4)

photo6 = PhotoImage(file = "/home/naina/naina_python/amazon.png")
photoimage6 = photo6.subsample(16, 16)

photo7 = PhotoImage(file = "/home/naina/naina_python/flipkart.png")
photoimage7 = photo7.subsample(4, 4)

photo8 = PhotoImage(file = "/home/naina/naina_python/calculator1.png")
photoimage8 = photo8.subsample(4, 4)

photo9 = PhotoImage(file = "/home/naina/naina_python/turtle.png")
photoimage9 = photo9.subsample(4, 4)

photo10 = PhotoImage(file = "/home/naina/naina_python/screenshot1.png")
photoimage10 = photo10.subsample(8, 8)

photo11 = PhotoImage(file = "/home/naina/naina_python/maze1.png")
photoimage11 = photo11.subsample(10, 10)

photo12 = PhotoImage(file = "/home/naina/naina_python/firefox.png")
photoimage12 = photo12.subsample(25, 25)

photo13 = PhotoImage(file = "/home/naina/naina_python/chrome.png")
photoimage13 = photo13.subsample(6, 6)

photo14 = PhotoImage(file = "/home/naina/naina_python/vim.png")
photoimage14 = photo14.subsample(6, 6)

photo15 = PhotoImage(file = "/home/naina/naina_python/editor.png")
photoimage15 = photo15.subsample(6, 6)

photo16 = PhotoImage(file = "/home/naina/naina_python/vlc.png")
photoimage16 = photo16.subsample(6, 6)

photo17 = PhotoImage(file = "/home/naina/naina_python/software.png")
photoimage17 = photo17.subsample(10, 10)

photo18 = PhotoImage(file = "/home/naina/naina_python/fileman.png")
photoimage18 = photo18.subsample(6, 6)

photo19 = PhotoImage(file = "/home/naina/naina_python/cheese.png")
photoimage19 = photo19.subsample(8, 8)

photo20 = PhotoImage(file = "/home/naina/naina_python/shotwell.png")
photoimage20 = photo20.subsample(10, 10)

#trash----------------
photo21 = PhotoImage(file = "/home/naina/naina_python/shotwell.png")
photoimage21 = photo21.subsample(10, 10)
#------------------------------------------------------------------------------------------------

#shutdown
button4 = Button( text="shutdown", fg="red", image=photoimage4,command = fol.main )
button4.grid(row = 0, column = 11) 
#restart
button5 = Button( text="restart", fg="red" , image=photoimage5,command = restart.main)
button5.grid(row = 0, column = 10) 

button10 = Button( text="screenshot", fg="red" , image=photoimage10,command = screenshot.main)
button10.grid(row = 0, column = 9) 
#-------------------------------------------------------


button2 = Button( text="google", fg="red",image=photoimage2, command = browser.main)
button2.grid(row = 5, column = 5,padx = 50,pady = 10) 
messageVar2 = Message(root, text = "Google it",width = 100)
messageVar2.config(bg='lightgreen')
messageVar2.grid(row = 6, column = 5,padx = 50,pady = 10) 

#----------------------------------------------------------------

button3 = Button( text="terminal", fg="red", image=photoimage3,command = function1.main)
button3.grid(row = 7, column = 5,padx = 50,pady = 10) 
messageVar3 = Message(root, text = "terminal",width = 100)
messageVar3.config(bg='lightgreen')
messageVar3.grid(row = 8, column = 5,padx = 50,pady = 10) 

#-----------------------------------------------------------------------

button6 = Button( text="restart", fg="red" , image=photoimage6,command = amo.main)
button6.grid(row = 9, column = 5,padx = 50,pady = 10) 
messageVar6 = Message(root, text = "amazon",width = 100) 
messageVar6.config(bg='lightgreen')
messageVar6.grid(row = 10, column = 5,padx = 50,pady = 10) 

#-----------------------------------------------------------

button12 = Button( text="firefox", fg="red" , image=photoimage12,command = user.main)
button12.grid(row = 11, column = 5,padx = 50,pady = 10) 
messageVar12 = Message(root, text = "firefox",width = 100) 
messageVar12.config(bg='lightgreen')
messageVar12.grid(row = 12, column = 5,padx = 50,pady = 10) 



def new():
    root1 = Toplevel(root)
    
   
    button2 = Button( root1,text="google", fg="red",image=photoimage2, command = browser.main)
    button2.grid(row = 5, column = 7,padx = 50,pady = 10) 
    messageVar2 = Message(root1, text = "Google it",width = 100)
    messageVar2.config(bg='lightgreen')
    messageVar2.grid(row = 6, column = 7,padx = 50,pady = 10) 

    #----------------------------------------------------------------

    button3 = Button( root1,text="terminal", fg="red", image=photoimage3,command = function1.main)
    button3.grid(row = 5, column = 8,padx = 50,pady = 10) 
    messageVar3 = Message(root1, text = "terminal",width = 100)
    messageVar3.config(bg='lightgreen')
    messageVar3.grid(row = 6, column = 8,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------

    button6 = Button( root1,text="restart", fg="red" , image=photoimage6,command = amo.main)
    button6.grid(row = 5, column = 9,padx = 50,pady = 10) 
    messageVar6 = Message(root1, text = "amazon",width = 100) 
    messageVar6.config(bg='lightgreen')
    messageVar6.grid(row = 6, column = 9,padx = 50,pady = 10) 

    #-----------------------------------------------------------

    button7 = Button( root1,text="restart", fg="red" , image=photoimage7,command = flip.main)
    button7.grid(row = 5, column = 10,padx = 50,pady = 10) 
    messageVar7 = Message(root1, text = "filkart",width = 100) 
    messageVar7.config(bg='lightgreen')
    messageVar7.grid(row = 6, column = 10,padx = 50,pady = 10) 

    #--------------------------------------------------------------------------

    button8 = Button( root1,text="calculator", fg="red" , image=photoimage8,command = flip.main)
    button8.grid(row = 5, column = 11,padx = 50,pady = 10) 
    messageVar8 = Message(root1, text = "Calculator",width = 150) 
    messageVar8.config(bg='lightgreen')
    messageVar8.grid(row = 6, column = 11,padx = 50,pady = 10) 
    #--------------------------------------------------------------------------

    button12 = Button( root1,text="firefox", fg="red" , image=photoimage12,command = user.main)
    button12.grid(row = 11, column = 6,padx = 50,pady = 10) 
    messageVar12 = Message(root1, text = "firefox",width = 100) 
    messageVar12.config(bg='lightgreen')
    messageVar12.grid(row = 12, column = 6,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------

    button13 = Button(root1, text="chrome", fg="red" , image=photoimage13,command = chrome.main)
    button13.grid(row = 11, column = 7,padx = 50,pady = 10) 
    messageVar13 = Message(root1, text = "chrome",width = 100) 
    messageVar13.config(bg='lightgreen')
    messageVar13.grid(row = 12, column = 7,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------

    button14 = Button( root1,text="chrome", fg="red" , image=photoimage14,command = vi.main)
    button14.grid(row = 11, column = 8,padx = 50,pady = 10) 
    messageVar14 = Message(root1, text = "vi",width = 100) 
    messageVar14.config(bg='lightgreen')
    messageVar14.grid(row = 12, column = 8,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------
    button15 = Button(root1, text="chrome", fg="red" , image=photoimage15,command = editor.main)
    button15.grid(row = 11, column = 9,padx = 50,pady = 10) 
    messageVar15 = Message(root1, text = "editor",width = 100) 
    messageVar15.config(bg='lightgreen')
    messageVar15.grid(row = 12, column = 9,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------
    button16 = Button(root1, text="chrome", fg="red" , image=photoimage16,command = vlc.main)
    button16.grid(row = 11, column = 10,padx = 50,pady = 10) 
    messageVar16 = Message(root1, text = "vlc",width = 100) 
    messageVar16.config(bg='lightgreen')
    messageVar16.grid(row = 12, column = 10,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------
    button17 = Button( root1,text="chrome", fg="red" , image=photoimage17,command = ubuntusoftware.main)
    button17.grid(row = 11, column = 11,padx = 50,pady = 10) 
    messageVar17 = Message(root1, text = "software",width = 100) 
    messageVar17.config(bg='lightgreen')
    messageVar17.grid(row = 12, column = 11,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------
    button18 = Button( root1,text="chrome", fg="red" , image=photoimage18,command = filemanager.main)
    button18.grid(row = 11, column = 12,padx = 50,pady = 10) 
    messageVar18 = Message(root1, text = "File manager",width = 100) 
    messageVar18.config(bg='lightgreen')
    messageVar18.grid(row = 12, column = 12,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------
    button19 = Button( root1,text="chrome", fg="red" , image=photoimage19,command = cheese.main)
    button19.grid(row = 11, column = 13,padx = 50,pady = 10) 
    messageVar19 = Message(root1, text = "cheese",width = 100) 
    messageVar19.config(bg='lightgreen')
    messageVar19.grid(row = 12, column = 13,padx = 50,pady = 10) 

    #-----------------------------------------------------------------------------
    button20 = Button( root1,text="chrome", fg="red" , image=photoimage20,command = shotwell.main)
    button20.grid(row = 13, column = 6,padx = 50,pady = 10) 
    messageVar20 = Message(root1, text = "shotwell",width = 100) 
    messageVar20.config(bg='lightgreen')
    messageVar20.grid(row = 14, column = 6,padx = 50,pady = 10) 

    #------------------------------------------------------------------------
    button21 = Button( root1,text="trash", fg="red" , image=photoimage21,command = trash.main)
    button21.grid(row = 13, column = 7,padx = 50,pady = 10) 
    messageVar21 = Message(root1, text = "trash",width = 100) 
    messageVar21.config(bg='lightgreen')
    messageVar21.grid(row = 14, column = 7,padx = 50,pady = 10) 




def new2():
    root2 = Toplevel(root)
    button1 = Button(root2, text="age", fg="red", image=photoimage1, command=aging.main)
    button1.grid(row = 5, column = 6,padx = 50,pady = 10) 
    messageVar1 = Message(root2, text = "get your age",width = 150) 
    messageVar1.config(bg='lightgreen')
    messageVar1.grid(row = 6, column = 6,padx = 50,pady = 10) 

    #------------------------------------------------------------


 
    #---------------------------------------------------------------------------

    button9 = Button(root2, text="restart", fg="red" , image=photoimage9,command = snake.main)
    button9.grid(row = 5, column = 12,padx = 50,pady = 10) 
    messageVar9 = Message(root2, text = "turtle race",width = 100) 
    messageVar9.config(bg='lightgreen')
    messageVar9.grid(row = 6, column = 12,padx = 50,pady = 10) 

    #---------------------------------------------------------------------------

    button11 = Button(root2, text="maze u", fg="red" , image=photoimage11,command = snake.main)
    button11.grid(row = 5, column = 13,padx = 50,pady = 10) 
    messageVar11 = Message(root2, text = "maze u",width = 100) 
    messageVar11.config(bg='lightgreen')
    messageVar11.grid(row = 6, column = 13,padx = 50,pady = 10) 



button21 = Button( text="all", fg="red",command = new)
button21.grid(row = 13, column = 5,padx = 50,pady = 10) 


button22 = Button( text="new app", fg="red",command = new2)
button22.grid(row = 15, column = 5,padx = 50,pady = 10)

root.mainloop()