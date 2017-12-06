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
from Flower_Class import Flower
from Point_Class import Point


def main():
    """
    Makes two flowers with geometric patterns.
    :return: None
    """
    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgcolor("green")             # Set up screen color
    #wn.bgpic("giphy.gif")
    p = Point(30, -47)
    dani = Flower(p)
    dani.user_set_size()
    dani.grow_flower_a()
    #dani.grow_flower_b()
    #dani.grow_steams()
    p1 = Point(-200, 100)
    ella = Flower(p1)
    ella.user_set_size()
    ella.grow_flower_b()
    wn.onclick(ella.flower_center)
    wn.mainloop()

main()
