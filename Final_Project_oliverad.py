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
from time import sleep


def instructions():
    name = input("Hello there! What is your name? \n")
    print("Welcome, {0}! This program will help you create a beautiful garden". format(name))
    sleep(delay)
    print("Answer the questions and once the flowers are drawn, click on the center each flower to add a flower center")
    sleep(delay)
    print("You can also add butterflies! Just press b and they will come to your garden.")
    sleep(delay)
    print("After your garden is ready, press q to exit")
    sleep(delay)
    print("Let's begin!")
    sleep(delay)


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
    global delay
    delay = 1.5
    instructions()
    wn = turtle.Screen()            # Makes a new turtle screen
    wn.title("A beautiful garden")
    wn.bgpic("grass.gif")
    p = Point()                     # Point object created at 0,0 by default
    butterfly = Butterfly()
    flowers = int(input("How many flowers dou you want? Suggested: 1-4 \n"))
    while flowers == 0 or flowers > 4:
        msg = "CANNOT DRAW {0} FLOWERS".format(flowers)
        print(msg)
        flowers = int(input("How many flowers dou you want? Suggested: 1-4 \n"))

    else:
        for i in range(flowers):
            global dani
            sleep(delay)
            print("Now you have to enter the x and y coordinate points where you want your flower")
            sleep(delay)
            print("Suggested values are between -200 and 200 for x and between -20 and 90 for y")
            sleep(delay)
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
