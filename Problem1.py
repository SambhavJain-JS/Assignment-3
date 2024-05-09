from turtle import Turtle

pattern=Turtle()

def repeat_shape():
    for i in range(15):
        pattern.forward(50)
        pattern.left(90)
        pattern.forward(50)
        pattern.left(90)
        pattern.forward(50)
        pattern.left(90)
        pattern.forward(50)
        pattern.left(90)
        pattern.left(30)

print(repeat_shape())
