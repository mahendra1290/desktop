'''from graphics import *
from button import Button
from math import pi, e, sin, cos, tan, log, log10, exp, sqrt
class Calculator:
    # This class implements a simple calculator GUI
    def __init__(self):
        # create the window for the calculator
        win = GraphWin("calculator")
        win.setCoords(0,0,9,13.5)   #from (0,0,6,7)
        win.setBackground("slategray")
        self.win = win
        # Now create the widgets
        self.__createButtons()
        self.__createDisplay()
    def __createButtons(self):
        # create list of buttons
        # start with all the standard sized buttons
        # bSpecs gives center coords and label of buttons
        bSpecs = [(2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C')]
        self.buttons = []
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))
        # create the larger = button
        self.buttons.append(Button(self.win, Point(4.5,1), 1.75, .75, "="))
        # activate all buttons
        for b in self.buttons:  b.activate()
    def __createDisplay(self):
        bg = Rectangle(Point(.5,12), Point(8.5,13))   #from (.5,5.5), (5.5,6.5)
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(4.5,12.5), "")   #from (3,6)
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(12)
        self.display = text
    def getButton(self):
        # Waits for a button to be clicked and returns the label of
        #    the button that was clicked.
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel() # method exit
    def processButton(self, key):
        # Updates the display of the calculator for press of this key
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            # Backspace, slice off the last character.
            self.display.setText(text[:-1])
        elif key == '=':
            # Evaluate the expresssion and display the result.
            # the try...except mechanism "catches" errors in the
            # formula being evaluated.
            try:
                result = eval(text)
            except: result = 'ERROR'
            self.display.setText(str(result))
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text+key)
        
    def run(self):
        # Infinite 'event loop' to process button clicks.
        while True:
            key = self.getButton()
            self.processButton(key)
# This runs the program.
if __name__ == '__main__':
    # First create a calculator object
    theCalc = Calculator()
    # Now call the calculator's run method.
    theCalc.run()'''
from tkinter import *
 
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
    storeObj.pack(side=side, expand =YES, fill =BOTH)
    return storeObj
 
def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand = YES, fill=BOTH)
    return storeObj
 
class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill =BOTH)
        self.master.title('Calculator')
 
        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,
          justify='right'
          , bd=30, bg="powder blue").pack(side=TOP,
                                          expand=YES, fill=BOTH)
 
        for clearButton in (["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearButton:
                button(erase, LEFT, ichar, lambda
                    storeObj=display, q=ichar: storeObj.set(''))
 
        for numButton in ("789/", "456*", "123-", "0.+"):
         FunctionNum = iCalc(self, TOP)
         for iEquals in numButton:
            button(FunctionNum, LEFT, iEquals, lambda
                storeObj=display, q=iEquals: storeObj
                   .set(storeObj.get() + q))
 
        EqualButton = iCalc(self, TOP)
        for iEquals in "=":
            if iEquals == '=':
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
 
 
            else:
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                    (storeObj.get() + s))
 
    def calc(self, display):
            try:
                display.set(eval(display.get()))
            except:
                display.set("ERROR")
 
 
def main():
 app().mainloop()