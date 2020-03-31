from PIL import Image 
  
def main(): 
    try: 
        
        img = Image.open("calculator1.png")  
        img.show()  
        
        img = img.rotate(180)  
       
        #img.save("rotated_picture.png") 
    except IOError: 
        pass
  
if __name__ == "__main__": 
    main()