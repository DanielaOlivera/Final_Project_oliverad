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
from Butterfly_Class import Butterfly


def h1():
    """
    Event handler to close window
    :return: None
    """
    wn.bye()                        # Close down the turtle window


def h2():
    """
    Event handler to stamp butterflies
    :return:
    """
    butterfly.stamp_butterfly()     # Stamp butterfly


def main():
    """
    Makes two flowers with geometric patterns.
    :return: None
    """
    global wn
    global butterfly
    wn = turtle.Screen()            # Makes a new turtle screen
    wn.bgpic("grass.gif")
    p = Point()                     # Point object created at 0,0 by default
    butterfly = Butterfly()
    flowers = int(input("How many flowers dou you want? Suggested: 1-4"))
    while flowers == 0 or flowers > 4:
        msg = "CANNOT DRAW {0} FLOWERS".format(flowers)
        print(msg)
        flowers = int(input("How many flowers dou you want? Suggested: 1-4"))

    else:
        for i in range(flowers):
            global dani
            p.user_set()                    # Point object is updated according to user input
            dani = Flower(p)
            dani.user_set_shape_petals()    # Ask user for number of sides in each petal
            dani.user_set_size()            # Ask user for size of sides in each petal
            if dani.petal_sides == 3:
                dani.grow_flower_a()        # Draw flower with triangles in each petal
            if dani.petal_sides == 5:
                dani.grow_flower_b()        # Draw flower with pentagons in each petal

    wn.onclick(dani.flower_center)      # Stamp a yellow circle where the user clicks
    wn.onkey(h1, "q")    # press q to quit
    wn.onkey(h2, "b")    # press b to stamp butterflies
    wn.listen()          # this enables the window to listen to onkey events
    wn.mainloop()


main()
