# fidget spinner game using python
# I am going to use Python Turtle module
# which is a drawing board where I can command a turtle to draw all over it

# import object from module turtle
from turtle import *

# initial state of the spinner is null
state = {'turn': 0}


# draw fidget spinner
def spin():
    clear()
    # angle of the fidget spinner
    angle = state["turn"] / 10

    # To rotate in clock wise  use right
    # for Anticlockwise rotation use left

    right(angle)
    # move the turtle forward by specified distance
    forward(100)
    # draw a dot with diameter 120 using colour red
    dot(120, "violet")
    # move the turtle backward by specified distance
    back(100)

    "second dot"
    right(120)
    forward(100)
    dot(120, "cyan")
    back(100)

    "third dot"
    right(120)
    forward(100)
    dot(120, "red")
    back(100)
    right(120)
    update()


# animate fidget spinner
def animate():
    if state['turn'] > 0:
        state['turn'] -= 1
    spin()
    ontimer(animate, 20)


# flick fidget spinner
def flick():
    state['turn'] += 40  # acceleration of spinner


# setup window screen
setup(600, 400, 370, 0)
bgcolor("black")
tracer(False)
# wing of fidget spinner
width(60)
color("green")
# keyboard key for the rotation of spinner
onkey(flick, "space")

listen()
animate()
done()