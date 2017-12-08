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
import random


class Butterfly:
    """
    A butterfly object
    """
    def __init__(self):
        """
        Creates flowers at a starting position
        """
        self.turtle = turtle.Turtle()
        self.wn = turtle.Screen()
        self.wn.addshape("butterfly1.gif")

    def draw_butterfly(self):

        self.turtle.pensize(5)
        self.turtle.color("orange")
        self.turtle.penup()
        self.turtle.goto(random.randint(-200, 200), random.randint(-200,200))
        self.turtle.shape("butterfly1.gif")
        self.turtle.stamp()
