from asyncio import SendfileNotAvailableError
import string
import turtle
from typing import Tuple
import random

AXIOM = "a" #Axiom of the gramatic (consult README)
N = 10 #Number of times that the rules will be apply 

def apply_rules(curve: string) -> string:
    """ 
    Apply derivation rules to a string that belogs to the gramatic alphabet 
    (consult README)
    """
    curve = curve.replace("a","-Bf+AfA+fB-")  
    curve = curve.replace("b","+Af-BfB-fA+")
    return curve.lower()

def pick_color() -> Tuple[int, int, int]:
    """ 
    Create a color with the rgb agreement 
    """
    color = (0, 0, 0)
    while color == (0, 0, 0):
        color = tuple(random.randint(0, 255) for _ in range(3))
    return color


def pain_curve(
    curve: string, line_lenght: float, pen: turtle.Turtle, angle: float, 
) -> None:
    """
    Paints the  Hilbert Curve

    Parameters
    ----------
    curve: string
        String of all the productions
    line_lengh : float
        Lenght of the line
    pen : turtle.Turtle
        Pen to paint
    angle : int
        Angle for change the displacement
    """

    for c in curve:
        pen.color(pick_color())
        if c == 'f':
            pen.forward(line_lenght)
        elif c == '+':
            pen.left(angle)
        elif c == '-':
            pen.right(angle)

# Initial settings to turtle module
window = turtle.Screen()
window.bgcolor("black")
turtle.colormode(255)

# Pen setup
my_pen = turtle.Turtle()
my_pen.speed(-200)
my_pen.left(90)
my_pen.penup()
my_pen.setpos(0, -250)
my_pen.pendown()
my_pen.hideturtle()
my_pen.pensize(2)

curve = AXIOM
for i in range(N):
    curve = apply_rules(curve)

curve = curve.replace("a","")
curve = curve.replace("b","")
pain_curve(curve, 5, my_pen, 90)
window.exitonclick()