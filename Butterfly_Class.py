######################################################################
# Author: Daniela Olivera
# Username: oliverad
#
# Assignment: Final Project
# Purpose: Introduces the use of functions with the turtle library
######################################################################
# Acknowledgements:
# Scott Heggen
#################################################################################
import turtle


class Butterfly:
    """
    A butterfly object
    """
    def __init__(self, pos):
        """
        Creates flowers at a starting position
        """
        self.initial_position = pos  # A Point object to hold the starting position
        self.turtle = turtle.Turtle()
        self.wn = turtle.Screen()

    def draw_butterfly(self):

        self.turtle.pensize(5)
        self.turtle.color("orange")
        self.turtle.penup()
        self.turtle.goto(34,90)
        self.turtle.hideturtle()
        self.turtle.pendown()
        self.turtle.begin_fill()
        for i in range(2):
            self.turtle.circle(10, 180)
            self.turtle.left(-90)
            self.turtle.forward(3)
        self.turtle.end_fill()
        self.turtle.right(45)
        for h in range(3):
            self.turtle.color("black")# draw body
            self.turtle.forward(-12)
            self.turtle.right(-3)
