from turtle import *
from random import randint
def main():
    speed(6)
    penup()
    goto(-180,180)

    for step in range(17):
        write(step,align = 'center')
        right(98)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(98)
        forward(20)

#----------------------------------
    ada = Turtle()
    ada.color('red')
    ada.shape('turtle')
    ada.penup()
    ada.goto(-180,160)
    ada.pendown()
    #----------------------------------
    bob = Turtle()
    bob.color('blue')
    bob.shape('turtle')
    bob.penup()
    bob.goto(-185,100)
    bob.pendown()
    #----------------------------------
    a = Turtle()
    a.color('pink')
    a.shape('turtle')
    a.penup()
    a.goto(-190,40)
    a.pendown()
    #----------------------------------
    b = Turtle()
    b.color('green')
    b.shape('turtle')
    b.penup()
    b.goto(-195,-20)
    b.pendown()
    #----------------------------------
    for turn in range (100):
        ada.forward(randint(1,5))
        bob.forward(randint(1,5))
        a.forward(randint(1,5))
        b.forward(randint(1,5))



