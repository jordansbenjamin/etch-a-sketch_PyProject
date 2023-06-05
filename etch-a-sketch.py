from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

pen.shape('classic')

# Forwards
def forwards():
    pen.forward(10)

# Backwards

# Rotate counter-clockwise (left)

# Rotate clockwise (right)

# Clear drawing

screen.listen()

screen.onkey(key='w', fun=forwards)

screen.exitonclick()