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
        Creates butterfly shapes
        """
        self.turtle = turtle.Turtle()
        self.wn = turtle.Screen()
        self.wn.addshape("butterfly1.gif")

    def stamp_butterfly(self):
        """
        Stamps a butterfly at a random point
        :return: None
        """
        self.turtle.pensize(5)
        self.turtle.color("orange")
        self.turtle.penup()
        self.turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.turtle.shape("butterfly1.gif")
        self.turtle.stamp()
