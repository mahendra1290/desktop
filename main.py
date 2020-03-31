#----------------------------------------------LOGIN PAGE CODE-----------------------------------------
from  tkinter import* 
#import PIL #import ImageTK
class Login_System :
    def __init__(self,root):
        self.root = root 
        self.root.title("User ID")
        self.root.geometry("1350x700+0+0")
        
        #images,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        

        #


        title = Label (self.root,text = "Sign in",font = ("times new roman",35),bg = "purple",height = 3,width = 1)
        title.place(x = 0,y = 0,relwidth = 1)
        login_frame = Frame(self.root,bg = "black")
        login_frame.place(x = 500,y = 400)
        lbluser = Label(login_frame,text = "naina",font = ("time new roman",20),bg = "grey").grid(row = 1,column = 1,padx = 20,pady =10)
        

        lblpass = Label(login_frame,text = "password",font = ("time new roman",20),bg = "grey").grid(row = 2,column = 0,padx = 20,pady =10)
        txtpass = Entry (login_frame,bd = 5,relief = GROOVE,font=("",15)).grid(row=2,column =1 ,padx=20)
        btn_log = Button(login_frame,text="check",font=("times new roman",14),bg = "yellow",fg="red").grid(row = 3,column = 1,pady = 10)


        


root = Tk()
obj = Login_System(root)
root.mainloop()      
