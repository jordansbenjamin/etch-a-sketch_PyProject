from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

pen.shape('classic')

# Forwards
def forwards():
    pen.forward(10)

# Backwards
def backwards():
    pen.backward(10)

# Rotate counter-clockwise (left)

# Rotate clockwise (right)

# Clear drawing

screen.listen()

screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)

screen.exitonclick()