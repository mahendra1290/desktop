#----------------------------------------------AGE CACLULATOR PAGE CODE-----------------------------------------
from tkinter import * 
from tkinter import messagebox 
  
def clearAll() : 
    dayField.delete(0, END) 
    monthField.delete(0, END) 
    yearField.delete(0, END) 
    givenDayField.delete(0, END) 
    givenMonthField.delete(0, END) 
    givenYearField.delete(0, END) 
    rsltDayField.delete(0, END) 
    rsltMonthField.delete(0, END) 
    rsltYearField.delete(0, END) 
   
def checkError() : 
    if (dayField.get() == "" or monthField.get() == "" 
        or yearField.get() == "" or givenDayField.get() == "" 
        or givenMonthField.get() == "" or givenYearField.get() == "") : 
        messagebox.showerror("Input Error") 
        clearAll() 
          
        return -1  

def calculateAge() : 

    value = checkError() 

    if value ==  -1 : 
        return
      
    else : 
        birth_day = int(dayField.get()) 
        birth_month = int(monthField.get()) 
        birth_year = int(yearField.get()) 
  
        given_day = int(givenDayField.get()) 
        given_month = int(givenMonthField.get()) 
        given_year = int(givenYearField.get()) 

        month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
          
        if (birth_day > given_day): 
            given_month = given_month - 1
            given_day = given_day + month[birth_month-1]  

        if (birth_month > given_month): 
            given_year = given_year - 1
            given_month = given_month + 12

        calculated_day = given_day - birth_day;  
        calculated_month = given_month - birth_month;  
        calculated_year = given_year - birth_year; 

        rsltDayField.insert(10, str(calculated_day)) 
        rsltMonthField.insert(10, str(calculated_month)) 
        rsltYearField.insert(10, str(calculated_year)) 
      

def main():
 
    gui = Tk() 
  
    gui.configure(background = "peach puff") 
  
    gui.title("do you want to know your age?") 

    gui.geometry("5000x5000") 
  
    
    dob = Label(gui, text = "Date Of Birth", bg = "DeepPink2",font = ("times new roman",35)) 
  
    givenDate = Label(gui, text = "Given Date", bg = "DeepPink2",font = ("times new roman",35)) 
 
    day = Label(gui, text = "Day", bg = "DeepPink2",font = ("times new roman",25)) 

    month = Label(gui, text = "Month", bg = "DeepPink2",font = ("times new roman",25)) 
  
    year = Label(gui, text = "Year", bg = "DeepPink2",font = ("times new roman",25)) 
  

    givenDay = Label(gui, text = "Given Day", bg = "DeepPink2",font = ("times new roman",25)) 
    givenMonth = Label(gui, text = "Given Month", bg = "DeepPink2",font = ("times new roman",25)) 
    givenYear = Label(gui, text = "Given Year", bg = "DeepPink2",font = ("times new roman",25)) 
  

    rsltYear = Label(gui, text = "Years", bg = "DeepPink2",font = ("times new roman",25)) 
    rsltMonth = Label(gui, text = "Months", bg = "DeepPink2",font = ("times new roman",25)) 
    rsltDay = Label(gui, text = "Days", bg = "DeepPink2",font = ("times new roman",25)) 

    resultantAge = Button(gui, text = "Resultant Age", fg = "Black", bg = "DeepPink2", command = calculateAge,font = ("times new roman",35)) 
    clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "DeepPink2", command = clearAll,font = ("times new roman",35)) 
  
  
    dayField = Entry(gui) 
    monthField = Entry(gui) 
    yearField = Entry(gui) 
      
    givenDayField = Entry(gui) 
    givenMonthField = Entry(gui) 
    givenYearField = Entry(gui) 
      
    rsltYearField = Entry(gui) 
    rsltMonthField = Entry(gui) 
    rsltDayField = Entry(gui) 
   
    dob.grid(row = 0, column = 6) 
      
    day.grid(row = 1, column = 5) 
    dayField.grid(row = 1, column = 6) 
      
    month.grid(row = 2, column = 5) 
    monthField.grid(row = 2, column = 6) 
      
    year.grid(row = 3, column = 5) 
    yearField.grid(row = 3, column = 6) 
      
    givenDate.grid(row = 0, column = 10) 
      
    givenDay.grid(row = 1, column = 9) 
    givenDayField.grid(row = 1, column = 10) 
      
    givenMonth.grid(row = 2, column = 9) 
    givenMonthField.grid(row = 2, column = 10) 
      
    givenYear.grid(row = 3, column = 9) 
    givenYearField.grid(row = 3, column = 10) 
      
    resultantAge.grid(row = 6, column = 8) 
      
    rsltYear.grid(row = 7, column = 8) 
    rsltYearField.grid(row = 8, column = 8) 
      
    rsltMonth.grid(row = 9, column = 8) 
    rsltMonthField.grid(row = 10, column = 8) 
      
    rsltDay.grid(row = 11, column = 8) 
    rsltDayField.grid(row = 12, column = 8) 
  
    clearAllEntry.grid(row = 14, column = 8) 
  
    # Start the GUI 
    gui.mainloop()