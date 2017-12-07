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


def h1():
    """
    Event handler to close window
    :return: None
    """
    wn.bye()                        # Close down the turtle window


def main():
    """
    Makes two flowers with geometric patterns.
    :return: None
    """
    global wn
    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgpic("grass.gif")
    p = Point()
    flowers = int(input("How many flowers dou you want?"))

    for i in range(flowers):
        global dani
        p.user_set()
        dani = Flower(p)
        dani.user_set_shape_petals()
        dani.user_set_size()
        if dani.petal_sides == 3:
            dani.grow_flower_a()
        if dani.petal_sides == 5:
            dani.grow_flower_b()

    wn.onclick(dani.flower_center)
    wn.onkey(h1, "q")
    wn.listen()
    wn.mainloop()


main()
