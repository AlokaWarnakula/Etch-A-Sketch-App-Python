from turtle import Turtle, Screen

aloka = Turtle()
screen = Screen()


def penUp():
    aloka.penup()


def penDown():
    aloka.pendown()


def moveForward():  # right
    aloka.setheading(0)
    aloka.forward(10)


def moveRightCircle():  # move right circle
    heading = aloka.heading() - 10
    aloka.setheading(heading)
    aloka.forward(10)


def moveBackward():  # left
    aloka.setheading(180)
    aloka.forward(10)


def moveLeftCircle():  # move left circle
    heading = aloka.heading() + 10
    aloka.setheading(heading)
    aloka.forward(10)


def moveUp():  # head
    aloka.setheading(90)
    aloka.forward(10)


def moveDown():  # back
    aloka.setheading(270)
    aloka.forward(10)


def clear():  # clear turtl drawing
    aloka.clear()


def reset():
    screen.reset()


def moveStraight():
    aloka.forward(10)


# when function add inside function parentheses not using

screen.listen()
screen.onkey(key="e", fun=penUp)
screen.onkey(key="q", fun=penDown)
screen.onkey(key="w", fun=moveUp)
screen.onkey(key="s", fun=moveDown)
screen.onkey(key="d", fun=moveForward)
screen.onkey(key="a", fun=moveBackward)
screen.onkey(key="z", fun=moveLeftCircle)
screen.onkey(key="x", fun=moveRightCircle)
screen.onkey(key="f", fun=moveStraight)
screen.onkey(key="c", fun=clear)
screen.onkey(key="r", fun=reset)

screen.exitonclick()
