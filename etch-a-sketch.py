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
def counter_clockwise():
    pen.left(10)

# Rotate clockwise (right)

# Clear drawing

screen.listen()

screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='a', fun=counter_clockwise)

screen.exitonclick()