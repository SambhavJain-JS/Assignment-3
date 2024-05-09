'''
Created on April 25, 2024

@author: Rushikesh
'''

from turtle import *

pg=Turtle()
wn = Screen()  # creates a graphics window


def func_name1(object):
    """This Functon print 'Welcome to ITC' ?"""
    

    # Drawing the first shape
    pg.penup()
    pg.goto(-100, 150)
    pg.pendown()
    pg.left(120)
    pg.forward(50)
    pg.goto(-100, 150)
    pg.right(60)
    pg.forward(25)
    pg.right(120)
    pg.forward(25)
    pg.left(120)
    pg.forward(50)

    # Drawing the second shape
    pg.penup()
    pg.goto(-45, 150)
    pg.pendown()
    pg.left(30)
    pg.forward(40)
    pg.right(90)
    pg.forward(30)
    pg.penup()
    pg.goto(-45, 170)
    pg.pendown()
    pg.forward(30)
    pg.penup()
    pg.goto(-45, 150)
    pg.pendown()
    pg.forward(30)

    # Drawing the third shape
    pg.penup()
    pg.goto(-10, 150)
    pg.pendown()
    pg.left(90)
    pg.forward(40)
    pg.backward(40)
    pg.right(90)
    pg.forward(30)
    

    # Drawing the fourth shape
    pg.penup()
    pg.goto(40, 150)
    pg.pendown()
    pg.circle(20, -180)

    # Drawing the fifth shape
    pg.penup()
    pg.goto(75, 190)
    pg.pendown()
    pg.circle(20)

    # Drawing the sixth shape
    pg.penup()
    pg.goto(105, 150)
    pg.pendown()
    pg.right(90)
    pg.forward(40)
    pg.right(145)
    pg.forward(30)
    pg.left(110)
    pg.forward(30)
    pg.right(145)
    pg.forward(40)

    # Drawing the seventh shape
    pg.penup()
    pg.goto(150, 150)
    pg.pendown()
    pg.left(150)
    pg.left(30)
    pg.forward(40)
    pg.right(90)
    pg.forward(30)
    pg.penup()
    pg.goto(150, 170)
    pg.pendown()
    pg.forward(30)
    pg.penup()
    pg.goto(150, 150)
    pg.pendown()
    pg.forward(30)

    # Drawing the eighth shape
    pg.penup()
    pg.goto(220, 150)
    pg.pendown()
    pg.left(90)
    pg.forward(40)
    pg.right(90)
    pg.forward(20)
    pg.backward(40)

    # Drawing the ninth shape
    pg.penup()
    pg.goto(260, 150)
    pg.pendown()
    pg.circle(20)

    # Drawing the tenth shape
    pg.penup()
    pg.goto(330, 150)
    pg.pendown()
    pg.left(90)
    pg.forward(40)
    pg.right(90)
    pg.forward(20)
    pg.backward(40)
    pg.penup()
    pg.goto(330, 150)
    pg.pendown()
    pg.forward(20)
    pg.backward(40)

    # Drawing the eleventh shape
    pg.penup()
    pg.goto(380, 150)
    pg.pendown()
    pg.left(90)
    pg.forward(40)
    pg.right(90)
    pg.forward(20)
    pg.backward(40)

    # Drawing the twelfth shape
    pg.penup()
    pg.goto(428, 150)
    pg.pendown()
    pg.circle(20, -180)




def func_name2(object):
    """It print house"""
    

    pg.teleport(-50,-100)
    pg.right(180)
    pg.fillcolor('yellow') 
    pg.begin_fill() 
    pg.right(90) 
    pg.forward(250) 
    pg.left(90) 
    pg.forward(400) 
    pg.left(90) 
    pg.forward(250) 
    pg.left(90) 
    pg.forward(400) 
    pg.right(90) 
    pg.end_fill() 

  
    pg.fillcolor('brown') 
    pg.begin_fill() 
    pg.right(45) 
    pg.forward(200) 
    pg.right(90) 
    pg.forward(200) 
    pg.left(180) 
    pg.forward(200) 
    pg.right(135) 
    pg.forward(259) 
    pg.right(90) 
    pg.forward(142) 
    pg.end_fill() 
    
    pg.teleport(300,-120)
    # pg.forward(50)
    pg.right(90)
    pg.forward(60)
    pg.left(90)
    pg.forward(60)
    pg.left(90)
    pg.forward(60)
    pg.left(90)
    pg.forward(60)
    pg.left(90)
    pg.forward(30)
    pg.left(90)
    pg.forward(60)
    pg.right(90)
    pg.forward(30)
    pg.right(90)
    pg.forward(30)
    pg.right(90)
    pg.forward(60)

    pg.teleport(-55,-350)
    pg.forward(120)
    pg.left(90)
    pg.forward(150)
    pg.left(90)
    pg.forward(35)
    pg.left(90)
    pg.forward(150)
    pg.right(90)
    pg.forward(10)
    pg.right(90)
    pg.forward(150)
    pg.right(90)
    pg.forward(10)
    pg.backward(40)
    pg.right(90)
    pg.forward(150)



def func_name3(object):
    """It print stick man"""
    
    pg.teleport(-310,-350)

    pg.penup()
    pg.goto(-330,-130)
    pg.pendown()
    pg.circle(20)

    # Body
    pg.penup()
    pg.goto(-310,-150)
    pg.setheading(270)  # Face downwards
    pg.pendown()
    pg.forward(70)

    # Right arm
    pg.penup()
    pg.goto(-310, -180)
    pg.left(120)  # Set the angle to draw arm
    pg.pendown()
    pg.forward(40)
    pg.backward(30)

    # Left arm
    pg.penup()
    pg.goto(-310, -180)
    pg.right(-110)  # Set the angle to draw arm
    pg.pendown()
    pg.forward(40)
    pg.backward(30)

    # Right leg
    pg.penup()
    pg.goto(-310, -220)
    pg.left(150)  # Set the angle to draw leg
    pg.pendown()
    pg.forward(50)
    pg.backward(50)

    # Left leg
    pg.penup()
    pg.goto(-310, -220)
    pg.left(-50)  # Set the angle to draw leg
    pg.pendown()
    pg.forward(50)
    pg.backward(50)



def func_name4(object):
    """This print Kite"""
    

    pg.teleport(-380,135)

    pg.forward(40)
    pg.fillcolor('red')
    pg.begin_fill()
    pg.left(120)
    pg.forward(40)
    pg.left(120)
    pg.forward(40)
    pg.end_fill()
    pg.pencolor("black")
    pg.penup()


    pg.left(110)
    pg.goto(-380,130)
    pg.pendown()
    pg.fillcolor("green")
    pg.begin_fill()
    pg.right(100)
    pg.forward(150)
    pg.right(90)
    pg.forward(150)
    pg.right(90)
    pg.forward(150)
    pg.right(90)
    pg.forward(150)
    pg.right(90)
    pg.end_fill()
    pg.right(45)
    pg.forward(210)
    pg.right(135)
    pg.right(45)
    pg.forward(75)
    pg.forward(55)

    pg.goto(-300,100)
    pg.goto(-368,264)
    pg.goto(-300,100)
    pg.goto(-280,-172)



def func_name5(object):
    """This print Flag"""
    
    pg.penup()
    pg.right(85)
    pg.goto(700, -220)
    pg.pendown()
    pg.color("orange")
    pg.begin_fill()
    pg.forward(80)
    pg.right(90)
    pg.forward(17)
    pg.right(90)
    pg.forward(80)
    pg.end_fill()


    pg.penup()
    pg.goto(700, -260)
    pg.pendown()
    
    pg.color("green")
    pg.right(-180)
    pg.begin_fill()
    pg.forward(80)
    pg.right(90)
    pg.forward(17)
    pg.right(90)
    pg.forward(80)
    pg.end_fill()


    pg.penup()
    pg.goto(660, -240)
    pg.pendown()
    pg.color("navy")
    pg.begin_fill()
    pg.circle(8)
    pg.end_fill()


    pg.penup()
    pg.goto(660, -237)
    pg.pendown()

    pg.color("white")
    pg.begin_fill()
    pg.circle(5)
    pg.end_fill()


    pg.penup()
    pg.color("black")
    pg.goto(620, -200)
    pg.right(180)
    pg.pendown()

    pg.begin_fill()
    pg.left(90)
    pg.forward(190)
    pg.right(90)
    pg.forward(8)
    pg.right(90)
    pg.forward(190)
    pg.right(90)
    pg.forward(8)
    pg.end_fill()

def func_name6(object):
    """It prints tree"""
    
    pg.up()
    pg.goto(-700,0)
    pg.down()
    pg.fillcolor('green')
    pg.begin_fill()
    pg.fd(120)
    pg.lt(130)
    pg.fd(95)
    pg.lt(100)
    pg.fd(95)
    pg.end_fill()

    # Middle trapezoid
    pg.setx(-675)
    pg.fillcolor('green')
    pg.begin_fill()
    pg.fd(100)
    pg.lt(130)
    pg.fd(200)
    pg.lt(130)
    pg.fd(100)
    pg.end_fill()

    # Bottom trapezoid
    pg.up()
    pg.setposition(-685,-76)
    pg.down()
    pg.fillcolor('green')
    pg.begin_fill()
    pg.lt(100)
    pg.fd(130)
    pg.lt(130)
    pg.fd(260)
    pg.lt(130)
    pg.fd(130)
    pg.end_fill()

    # Trunk
    pg.up()
    pg.setposition(-670,-155)
    pg.down()
    pg.fillcolor('brown')
    pg.begin_fill()
    pg.lt(140)
    pg.fd(50)
    pg.lt(90)
    pg.fd(60)
    pg.lt(90)
    pg.fd(50)
    pg.end_fill()

# Star on the top
    pg.up()
    pg.setposition(-670,90)
    pg.rt(90)
    pg.down()
    pg.fillcolor('yellow')
    pg.begin_fill()
    for i in range(5):
        pg.fd(60)
        pg.rt(144)
    pg.end_fill()


def func_name7(object):
    """This print sun"""
    pg.color('orange')
    pg.fillcolor('yellow')
    pg.pencolor('red')

    pg.up()
    pg.goto(-670,255)
    pg.down()


    for i in range(100):

        pg.begin_fill()

        pg.forward(10 - i)

        pg.left(170)

        pg.forward(10 - i)

        pg.end_fill()


def sketch():
    pg.speed(-5)
    func_name1(object)
    func_name2(object)
    func_name3(object)
    func_name4(object)
    func_name5(object)
    func_name6(object)
    func_name7(object)
    wn.exitonclick()


if __name__ == "__main__":
    sketch()
    
        
