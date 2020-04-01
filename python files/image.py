from tkinter import *
from PIL import Image
import os
path1 = "/home/naina/photos"   
path2 = "/home/naina/pic"   

listing = os.listdir(path1)    
for file in listing:
    im = Image.open(path1 + file)    
    im.resize((50,50))                            
    im.save(path2 + file, "JPEG")
master = Tk() 
mainloop()